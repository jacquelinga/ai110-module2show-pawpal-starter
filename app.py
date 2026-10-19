import streamlit as st
from datetime import time

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown("Add pets and their care tasks, then generate a schedule ordered by time.")

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="Jordan",
        availableTimeMinutes=60,
        preferences=[],
    )

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
pet_age = st.number_input("Pet age (years)", min_value=0, max_value=50, value=3)

if st.button("Add pet"):
    pet = Pet(name=pet_name.strip(), species=species, age=int(pet_age))
    st.session_state.owner.addPet(pet)

if st.session_state.owner.pets:
    st.write("Current pets:")
    st.table(
        [
            {"name": pet.name, "species": pet.species, "age": pet.age}
            for pet in st.session_state.owner.pets
        ]
    )
else:
    st.info("No pets added yet.")

st.markdown("### Tasks")
st.caption("Add a care task for one of your pets.")

if st.session_state.owner.pets:
    selected_pet = st.selectbox(
        "Pet",
        st.session_state.owner.pets,
        format_func=lambda pet: f"{pet.name} ({pet.species})",
    )
else:
    selected_pet = None
    st.info("Add a pet before adding tasks.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    task_time = st.time_input("Time", value=time(8, 0))

if st.button("Add task"):
    if selected_pet is None:
        st.warning("Add a pet before creating a task.")
    else:
        task = Task(
            name=task_title.strip(),
            durationMinutes=int(duration),
            priority=priority,
            category="care",
            time=task_time.strftime("%H:%M"),
        )
        Scheduler().addTask(selected_pet, task)

owner_tasks = st.session_state.owner.getAllTasks()
if owner_tasks:
    st.write("Current tasks:")
    st.table(
        [
            {
                "pet": pet.name,
                "task": task.name,
                "time": task.time,
                "duration (minutes)": task.durationMinutes,
                "priority": task.priority,
            }
            for pet in st.session_state.owner.pets
            for task in pet.tasks
        ]
    )
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Schedule")
st.caption("Tasks are ordered by time, and matching dates and times are flagged.")

if st.button("Generate schedule"):
    scheduler = Scheduler()
    scheduler.getTasks(st.session_state.owner)
    sorted_tasks = scheduler.sort_by_time()
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for conflict in conflicts:
            st.warning(conflict)
    else:
        st.success("No scheduling conflicts found.")

    if sorted_tasks:
        st.table(
            [
                {
                    "date": task.due_date.isoformat(),
                    "time": task.time,
                    "task": task.name,
                    "duration (minutes)": task.durationMinutes,
                    "priority": task.priority,
                }
                for task in sorted_tasks
            ]
        )
    else:
        st.info("No tasks to schedule yet.")
