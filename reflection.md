# PawPal+ Project Reflection

## 1. System Design

My initial UML design includes four main classes: Owner, Pet, Task, and Scheduler.

- Owner stores the owner's name, available time, and preferences.
- Pet stores basic information about the pet, including its name, species, and age.
- Task represents a pet care task and stores its name, duration, priority, and category.
- Scheduler manages the collection of tasks and is responsible for adding or editing tasks and generating a daily plan based on the owner's available time and preferences.
**b. Design changes**

After reviewing the class skeleton with AI, I noticed that the UML showed an Owner caring for one or more Pets, but the Owner class did not store any pets. I updated the Owner class to include a pet collection so this relationship is represented in the code.

I also changed the Scheduler's task collection from `tasks` to `_tasks` to better match the private attribute shown in the UML.


---

## 2. Scheduling Logic and Tradeoffs


- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
