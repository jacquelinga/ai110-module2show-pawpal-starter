from dataclasses import dataclass


class Owner:
	def __init__(
		self,
		name: str,
		availableTimeMinutes: int,
		preferences: list[str],
	) -> None:
		self.name = name
		self.availableTimeMinutes = availableTimeMinutes
		self.preferences = preferences

	def setAvailableTime(self, minutes: int) -> None:
		pass

	def updatePreferences(self, preferences: list[str]) -> None:
		pass


@dataclass
class Pet:
	name: str
	species: str
	age: int


@dataclass
class Task:
	name: str
	durationMinutes: int
	priority: str
	category: str

	def edit(
		self,
		name: str,
		durationMinutes: int,
		priority: str,
		category: str,
	) -> None:
		pass


class Scheduler:
	def __init__(self) -> None:
		self.tasks: list[Task] = []

	def addTask(self, task: Task) -> None:
		pass

	def editTask(self, task: Task) -> None:
		pass

	def generateDailyPlan(self, owner: Owner) -> list[Task]:
		pass
