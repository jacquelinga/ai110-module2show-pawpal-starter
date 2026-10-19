from pawpal_system import Pet, Task


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