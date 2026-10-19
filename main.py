from pawpal_system import Owner, Pet, Scheduler, Task


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
	scheduler.addTask(
		dog,
		Task(
			name="Morning walk",
			durationMinutes=25,
			priority="high",
			category="exercise",
			description="Take Mochi for a neighborhood walk",
		),
	)
	scheduler.addTask(
		dog,
		Task(
			name="Give medication",
			durationMinutes=5,
			priority="high",
			category="health",
			description="Give Mochi the daily tablet",
		),
	)
	scheduler.addTask(
		cat,
		Task(
			name="Breakfast",
			durationMinutes=10,
			priority="medium",
			category="feeding",
			description="Feed Miso",
		),
	)
	scheduler.addTask(
		cat,
		Task(
			name="Play session",
			durationMinutes=20,
			priority="low",
			category="play",
			description="Play with Miso",
		),
	)

	daily_plan = scheduler.generateDailyPlan(owner)

	print(f"Today's Schedule for {owner.name}")
	print(f"Available time: {owner.availableTimeMinutes} minutes")
	if daily_plan:
		for number, task in enumerate(daily_plan, start=1):
			print(
				f"{number}. {task.name} - {task.durationMinutes} min "
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