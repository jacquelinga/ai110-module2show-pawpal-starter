from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date, timedelta


class Owner:
	def __init__(
		self,
		name: str,
		availableTimeMinutes: int,
		preferences: list[str],
	) -> None:
		"""Initialize an owner and an empty pet list."""
		self.name = name
		self.availableTimeMinutes = availableTimeMinutes
		self.preferences = preferences
		self.pets: list["Pet"] = []

	def setAvailableTime(self, minutes: int) -> None:
		"""Update the owner's available time in minutes."""
		self.availableTimeMinutes = max(0, minutes)

	def updatePreferences(self, preferences: list[str]) -> None:
		"""Replace the owner's preference list."""
		self.preferences = list(preferences)

	def addPet(self, pet: Pet) -> None:
		"""Add a pet to the owner if it is not already present."""
		if pet not in self.pets:
			self.pets.append(pet)

	def getAllTasks(self) -> list[Task]:
		"""Return all tasks belonging to the owner's pets."""
		return [task for pet in self.pets for task in pet.tasks]


@dataclass
class Pet:
	name: str
	species: str
	age: int
	tasks: list[Task] = field(default_factory=list)

	def addTask(self, task: Task) -> None:
		"""Add a task to this pet if it is not already present."""
		if task not in self.tasks:
			self.tasks.append(task)


@dataclass
class Task:
	name: str
	durationMinutes: int
	priority: str
	category: str
	description: str = ""
	frequency: str = "daily"
	isComplete: bool = False
	time: str = "00:00"
	due_date: date = field(default_factory=date.today)

	def edit(
		self,
		name: str | None = None,
		durationMinutes: int | None = None,
		priority: str | None = None,
		category: str | None = None,
		description: str | None = None,
		frequency: str | None = None,
		isComplete: bool | None = None,
	) -> None:
		"""Update the task fields provided."""
		if name is not None:
			self.name = name
		if durationMinutes is not None:
			self.durationMinutes = durationMinutes
		if priority is not None:
			self.priority = priority
		if category is not None:
			self.category = category
		if description is not None:
			self.description = description
		if frequency is not None:
			self.frequency = frequency
		if isComplete is not None:
			self.isComplete = isComplete

	def mark_complete(self) -> Task | None:
		"""Mark this task complete and return its next recurring occurrence."""
		if self.isComplete:
			return None

		self.isComplete = True
		interval_days = {"daily": 1, "weekly": 7}.get(self.frequency)
		if interval_days is None:
			return None

		return Task(
			name=self.name,
			durationMinutes=self.durationMinutes,
			priority=self.priority,
			category=self.category,
			description=self.description,
			frequency=self.frequency,
			isComplete=False,
			time=self.time,
			due_date=self.due_date + timedelta(days=interval_days),
		)


class Scheduler:
	def __init__(self) -> None:
		"""Initialize an empty scheduler task list."""
		self._tasks: list[Task] = []

	def getTasks(self, owner: Owner) -> list[Task]:
		"""Return all tasks belonging to the owner's pets."""
		self._tasks = owner.getAllTasks()
		return list(self._tasks)

	def filter_tasks(
		self,
		owner: Owner,
		is_complete: bool | None = None,
		pet_name: str | None = None,
	) -> list[Task]:
		"""Filter owner tasks by completion status and/or pet name."""
		self.getTasks(owner)
		selected_pet_name = pet_name.strip().casefold() if pet_name and pet_name.strip() else None
		return [
			task
			for pet in owner.pets
			if selected_pet_name is None or pet.name.casefold() == selected_pet_name
			for task in pet.tasks
			if is_complete is None or task.isComplete == is_complete
		]

	def addTask(self, pet: Pet, task: Task) -> None:
		"""Add a task to the scheduler and its pet."""
		pet.addTask(task)
		if task not in self._tasks:
			self._tasks.append(task)

	def completeTask(self, pet: Pet, task: Task) -> Task | None:
		"""Complete a task and add its next recurring occurrence to the pet."""
		next_task = task.mark_complete()
		if next_task is not None:
			self.addTask(pet, next_task)
		return next_task

	def sort_by_time(self) -> list[Task]:
		"""Return the scheduler's tasks sorted by HH:MM time."""
		return sorted(self._tasks, key=lambda task: task.time)

	def detect_conflicts(self) -> list[str]:
		"""Return warnings for tasks with the same date and exact time."""
		tasks_by_time: dict[tuple[date, str], list[str]] = {}
		for task in self._tasks:
			date_and_time = (task.due_date, task.time)
			tasks_by_time.setdefault(date_and_time, []).append(task.name)

		return [
			f"Warning: {due_date.isoformat()} at {time} has multiple tasks: "
			f"{', '.join(task_names)}."
			for (due_date, time), task_names in tasks_by_time.items()
			if len(task_names) > 1
		]

	def editTask(
		self,
		task: Task,
		name: str | None = None,
		durationMinutes: int | None = None,
		priority: str | None = None,
		category: str | None = None,
		description: str | None = None,
		frequency: str | None = None,
		isComplete: bool | None = None,
	) -> None:
		"""Update the task with the supplied values."""
		task.edit(
			name=name,
			durationMinutes=durationMinutes,
			priority=priority,
			category=category,
			description=description,
			frequency=frequency,
			isComplete=isComplete,
		)

	def generateDailyPlan(self, owner: Owner) -> list[Task]:
		"""Build a priority-ordered plan within the owner's available time."""
		priority_order = {"high": 0, "medium": 1, "low": 2}
		preference_order = {
			category: index for index, category in enumerate(owner.preferences)
		}
		pending_tasks = [
			task
			for task in self.getTasks(owner)
			if not task.isComplete and task.due_date <= date.today()
		]
		pending_tasks.sort(
			key=lambda task: (
				priority_order.get(task.priority.lower(), 3),
				preference_order.get(task.category, len(preference_order)),
			)
		)

		remaining_minutes = owner.availableTimeMinutes
		daily_plan = []
		for task in pending_tasks:
			if task.durationMinutes <= remaining_minutes:
				daily_plan.append(task)
				remaining_minutes -= task.durationMinutes

		return daily_plan
