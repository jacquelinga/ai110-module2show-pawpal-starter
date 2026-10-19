from datetime import date, timedelta

from pawpal_system import Pet, Scheduler, Task


def test_mark_complete_changes_task_status() -> None:
	task = Task(
		name="Feed pet",
		durationMinutes=10,
		priority="high",
		category="feeding",
	)

	task.mark_complete()

	assert task.isComplete is True


def test_adding_task_increases_pet_task_count() -> None:
	pet = Pet(name="Mochi", species="dog", age=3)
	task = Task(
		name="Take a walk",
		durationMinutes=20,
		priority="medium",
		category="exercise",
	)
	initial_task_count = len(pet.tasks)

	pet.addTask(task)

	assert len(pet.tasks) == initial_task_count + 1


def test_sort_by_time_returns_tasks_in_chronological_order() -> None:
	scheduler = Scheduler()
	pet = Pet(name="Mochi", species="dog", age=3)
	late_task = Task(
		name="Evening walk",
		durationMinutes=20,
		priority="medium",
		category="exercise",
		time="18:30",
	)
	early_task = Task(
		name="Breakfast",
		durationMinutes=10,
		priority="high",
		category="feeding",
		time="07:00",
	)
	middle_task = Task(
		name="Lunch",
		durationMinutes=10,
		priority="medium",
		category="feeding",
		time="12:00",
	)

	scheduler.addTask(pet, late_task)
	scheduler.addTask(pet, early_task)
	scheduler.addTask(pet, middle_task)

	assert scheduler.sort_by_time() == [early_task, middle_task, late_task]


def test_completing_daily_task_creates_task_for_following_day() -> None:
	scheduler = Scheduler()
	pet = Pet(name="Mochi", species="dog", age=3)
	today = date(2026, 10, 18)
	task = Task(
		name="Feed pet",
		durationMinutes=10,
		priority="high",
		category="feeding",
		frequency="daily",
		due_date=today,
	)
	scheduler.addTask(pet, task)

	next_task = scheduler.completeTask(pet, task)

	assert task.isComplete is True
	assert next_task is not None
	assert next_task is not task
	assert next_task.due_date == today + timedelta(days=1)
	assert next_task.isComplete is False
	assert next_task in pet.tasks


def test_detect_conflicts_flags_tasks_at_same_date_and_time() -> None:
	scheduler = Scheduler()
	pet = Pet(name="Mochi", species="dog", age=3)
	due_date = date(2026, 10, 18)
	first_task = Task(
		name="Feed pet",
		durationMinutes=10,
		priority="high",
		category="feeding",
		time="08:00",
		due_date=due_date,
	)
	second_task = Task(
		name="Give medicine",
		durationMinutes=5,
		priority="high",
		category="health",
		time="08:00",
		due_date=due_date,
	)
	scheduler.addTask(pet, first_task)
	scheduler.addTask(pet, second_task)

	conflicts = scheduler.detect_conflicts()

	assert len(conflicts) == 1
	assert "2026-10-18 at 08:00" in conflicts[0]
	assert "Feed pet" in conflicts[0]
	assert "Give medicine" in conflicts[0]