# PawPal+ (Module 2 Project)

PawPal+ is a Streamlit-powered pet care planner that helps a busy owner keep track of multiple pets, manage recurring care tasks, and build a practical daily schedule based on time, priority, and personal preferences.

## Scenario

A busy pet owner needs help staying consistent with pet care. The application is designed to:

- Track pet care tasks such as walks, feeding, medication, grooming, and enrichment
- Consider constraints including available time, urgency, and owner preferences
- Generate a daily plan that prioritizes the most important tasks first
- Highlight scheduling problems such as overlapping tasks at the same time

The final system includes both the Python scheduling logic and a user-facing Streamlit interface.

## Features

PawPal+ includes the following features that are implemented in the final project:

- Pet and task management
  - Create owners and add multiple pets to their profile
  - Add tasks to a specific pet with time, priority, duration, and description
  - Track task status and recurring schedule metadata

- Sorting tasks by time
  - The scheduler orders tasks by their `HH:MM` time values for a clear daily view

- Filtering tasks
  - Filter tasks by pet name or completion status using the built-in scheduler logic

- Conflict warnings
  - Detect exact-date and exact-time overlaps and surface warnings when multiple tasks share the same time slot

- Daily and weekly recurring tasks
  - Completing a task can generate the next occurrence automatically, using a 1-day cycle for daily tasks and a 7-day cycle for weekly tasks

- Smarter scheduling
  - Build a priority-based daily plan that respects the owner's available time and preference order

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Review the app scenario and define the scheduling requirements.
2. Model your classes and relationships in UML.
3. Implement the core logic in Python for owner, pet, task, and scheduler behavior.
4. Add tests for the most important scheduling behaviors.
5. Connect the scheduling system to the Streamlit UI in `app.py`.
6. Verify the final implementation against the UML and update documentation as needed.

## Demo Walkthrough

The PawPal+ Streamlit app gives the user a simple workflow for building a care schedule:

1. Enter the owner's information and add a pet such as a dog or cat.
2. Add one or more tasks for that pet, including a title, duration, priority, and scheduled time.
3. Review the current pet/task list in the app and confirm the tasks are assigned correctly.
4. Generate the schedule to see all tasks sorted by time and any conflict warnings.
5. Use the daily plan to understand which tasks fit within the owner's available time and how the schedule was prioritized.

### User experience in the UI

- The app exposes fields for owner name, pet name, species, age, and task details.
- Users can create and manage multiple pets and their care tasks.
- The schedule view displays tasks by date and time, making it easy to scan a day at a glance.
- When two tasks share the same date and exact time, PawPal+ shows a warning so the owner can correct the conflict.
- Tasks are displayed in chronological order, which makes the schedule easier to follow.

### Example workflow

A typical user flow looks like this:

- Add a pet: `Mochi` (dog)
- Add a task: `Morning walk` at `08:00`, duration `25` minutes, priority `high`
- Add another task: `Give medication` at `07:00`, duration `5` minutes, priority `high`
- Generate the schedule and review the sorted time order
- Read any conflict warnings if tasks overlap
- Review the final daily plan built around the owner's available time

### Representative CLI output

```text
Schedule conflict check
  Warning: 2026-10-18 at 07:00 has multiple tasks: Breakfast, Give medication.

All tasks sorted by time
  2026-10-18 07:00 | Give medication - 5 min (high priority, pending)
  2026-10-18 07:00 | Breakfast - 10 min (medium priority, pending)
  2026-10-18 08:00 | Morning walk - 25 min (high priority, pending)
  2026-10-18 18:30 | Play session - 20 min (low priority, pending)
  2026-10-18 19:00 | Grooming - 15 min (low priority, pending)

Today's Priority-Based Plan for Jordan
Available time: 45 minutes
1. 07:00 - Give medication (5 min) (high priority, health)
   Give Mochi the daily tablet
2. 08:00 - Morning walk (25 min) (high priority, exercise)
   Take Mochi for a neighborhood walk
3. 19:00 - Grooming (15 min) (low priority, grooming)
   Brush Miso's coat
Total scheduled: 45 minutes
```

## Testing PawPal+

```bash
python3 -m pytest
```

The automated tests cover task addition and completion, chronological sorting, daily recurring tasks, and conflict detection.

```text
5 passed in 0.02s
```

**Confidence Level:** 5/5 stars

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Sorting tasks by time | `Scheduler.sort_by_time()` | Orders tasks by their `HH:MM` time. |
| Filtering by pet or completion status | `Scheduler.filter_tasks()` | Accepts optional pet-name and completion-status filters. |
| Daily and weekly recurring tasks | `Task.mark_complete()`, `Scheduler.completeTask()` | Creates the next occurrence one or seven days later and adds it to the pet. |
| Exact-time conflict detection | `Scheduler.detect_conflicts()` | Warns when tasks share the same date and time. |
| Daily plan generation | `Scheduler.generateDailyPlan()` | Builds a time-aware plan that respects owner availability and priority order. |

The final project balances pet care needs with practical constraints, letting the owner schedule work without overcommitting the day.
