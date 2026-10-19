# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Today's Schedule for Jordan
Available time: 45 minutes
1. Give medication - 5 min (high priority, health)
   Give Mochi the daily tablet
2. Morning walk - 25 min (high priority, exercise)
   Take Mochi for a neighborhood walk
3. Breakfast - 10 min (medium priority, feeding)
   Feed Miso
Total scheduled: 40 minutes
```

## Testing PawPal+

```bash
python3 -m pytest
```

The automated tests cover task addition and completion, chronological sorting, daily recurring tasks, and conflict detection.

```
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

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
