from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


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

	def mark_complete(self) -> None:
		"""Mark this task as completed."""
		self.isComplete = True


class Scheduler:
	def __init__(self) -> None:
		"""Initialize an empty scheduler task list."""
		self._tasks: list[Task] = []

	def getTasks(self, owner: Owner) -> list[Task]:
		"""Return all tasks belonging to the owner's pets."""
		self._tasks = owner.getAllTasks()
		return list(self._tasks)

	def addTask(self, pet: Pet, task: Task) -> None:
		"""Add a task to the scheduler and its pet."""
		pet.addTask(task)
		if task not in self._tasks:
			self._tasks.append(task)

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
		pending_tasks = [task for task in self.getTasks(owner) if not task.isComplete]
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
