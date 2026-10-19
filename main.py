from pawpal_system import Owner, Pet, Scheduler, Task


def display_tasks(title: str, tasks: list[Task]) -> None:
	print(f"\n{title}")
	if not tasks:
		print("  No tasks found.")
		return

	for task in tasks:
		status = "completed" if task.isComplete else "pending"
		print(
			f"  {task.due_date.isoformat()} {task.time} | "
			f"{task.name} - {task.durationMinutes} min "
			f"({task.priority} priority, {status})"
		)


def main() -> None:
	owner = Owner(
		name="Jordan",
		availableTimeMinutes=45,
		preferences=["health", "exercise", "feeding", "play"],
	)

	dog = Pet(name="Mochi", species="dog", age=3)
	cat = Pet(name="Miso", species="cat", age=2)
	owner.addPet(dog)
	owner.addPet(cat)

	scheduler = Scheduler()
	morning_walk = Task(
		name="Morning walk",
		durationMinutes=25,
		priority="high",
		category="exercise",
		description="Take Mochi for a neighborhood walk",
		time="08:00",
	)
	medication = Task(
		name="Give medication",
		durationMinutes=5,
		priority="high",
		category="health",
		description="Give Mochi the daily tablet",
		time="07:00",
	)
	breakfast = Task(
		name="Breakfast",
		durationMinutes=10,
		priority="medium",
		category="feeding",
		description="Feed Miso",
		time="07:00",
	)
	play_session = Task(
		name="Play session",
		durationMinutes=20,
		priority="low",
		category="play",
		description="Play with Miso",
		time="18:30",
	)
	grooming = Task(
		name="Grooming",
		durationMinutes=15,
		priority="low",
		category="grooming",
		description="Brush Miso's coat",
		frequency="weekly",
		time="19:00",
	)

	scheduler.addTask(dog, morning_walk)
	scheduler.addTask(dog, medication)
	scheduler.addTask(cat, breakfast)
	scheduler.addTask(cat, play_session)
	scheduler.addTask(cat, grooming)
	scheduler.completeTask(cat, grooming)

	conflict_warnings = scheduler.detect_conflicts()
	print("\nSchedule conflict check")
	if conflict_warnings:
		for warning in conflict_warnings:
			print(f"  {warning}")
	else:
		print("  No exact-time conflicts found.")

	display_tasks("All tasks sorted by time", scheduler.sort_by_time())
	display_tasks(
		"Tasks for Mochi",
		scheduler.filter_tasks(owner, pet_name="Mochi"),
	)
	display_tasks(
		"Tasks for Miso, including the next weekly occurrence",
		scheduler.filter_tasks(owner, pet_name="Miso"),
	)
	display_tasks(
		"Completed tasks",
		scheduler.filter_tasks(owner, is_complete=True),
	)

	daily_plan = scheduler.generateDailyPlan(owner)

	print(f"\nToday's Priority-Based Plan for {owner.name}")
	print(f"Available time: {owner.availableTimeMinutes} minutes")
	if daily_plan:
		for number, task in enumerate(daily_plan, start=1):
			print(
				f"{number}. {task.time} - {task.name} "
				f"({task.durationMinutes} min) "
				f"({task.priority} priority, {task.category})"
			)
			if task.description:
				print(f"   {task.description}")
		print(
			f"Total scheduled: "
			f"{sum(task.durationMinutes for task in daily_plan)} minutes"
		)
	else:
		print("No tasks fit the available time today.")


if __name__ == "__main__":
	main()