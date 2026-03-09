# 📘 HabitFlow — Habit Tracking Web Application

HabitFlow is a full‑stack Django web application designed to help users build, track, and maintain both positive and negative habits through daily logging, streaks, and progress insights. The project follows Agile methodology and is developed iteratively over a 7‑day sprint.

---

# 📑 Table of Contents

1. Project Overview  
2. Agile Planning  
3. User Stories  
4. Features  
5. Data Model  
6. Project Setup  
7. Development Log  
8. Documentation  
9. Tech Stack  
10. Security Notes  

---

# 📘 Project Overview

HabitFlow enables users to:

- Create habits  
- Track daily progress  
- Log completions or avoidance  
- View streaks and history  
- Maintain both positive and negative habits  

The application is built using Django, HTML, CSS, JavaScript, and Bootstrap.

---

# 🧭 Agile Planning

HabitFlow is developed using Agile methodology with a Kanban‑style GitHub Project Board:

**Project Board:**  
https://github.com/users/thejog2/projects/7

Work progresses through:

- To Do  
- In Progress  
- In Review  
- Done  

---

# 🧑‍💻 User Stories

### Authentication
- US01: Register an account  
- US02: Log in  
- US03: Log out  

### Habit Management
- US04: Create habits  
- US05: Edit habits  
- US06: Delete habits  

### Daily Logging
- US07: Log daily progress  
- US08: View log history  

### Dashboard
- US09: View today’s habits  
- US10: View streaks  

### UX & Accessibility
- US11: Responsive design  
- US12: Accessibility support  

### Deployment
- US13: Deploy the project  

---

# ⭐ Features

### ✔ User Authentication  
Registration, login, logout, and dynamic navigation.

### ✔ Profile System  
Each user has a Profile with a role (`user` or `admin`).

### ✔ Habit Tracking  
Users can create positive or negative habits.

### ✔ Daily Logging  
Users can log completion or avoidance for each habit.

### ✔ Admin Tools  
Admin users see additional navigation options.

### ✔ Responsive UI  
Bootstrap‑powered layout with custom CSS.

---

# 🖼️ Wireframes

These low‑fidelity wireframes outline the planned layout for the key pages in HabitFlow. They focus on structure and user flow rather than styling, and serve as a bridge between the data model (Day 3) and the UI implementation (Day 4 onward).

---

## 🏠 Dashboard (Today’s Habits)

```
+-----------------------------------------------------------+
|                        DASHBOARD                          |
+-----------------------------------------------------------+
|  Hello, {{ username }}                                    |
|  Today: {{ date }}                                        |
+-----------------------------------------------------------+
|  HABITS FOR TODAY                                         |
|                                                           |
|  [✓] Drink Water (Positive)        [Mark as Done]         |
|  [ ] No Sugar (Negative)           [Mark as Avoided]      |
|  [ ] Read 20 Minutes (Positive)    [Mark as Done]         |
|                                                           |
+-----------------------------------------------------------+
|  View All Habits | View Log History                       |
+-----------------------------------------------------------+
```

---

## 📋 Habit List Page
```
+-----------------------------------------------------------+
|                      HABIT DETAILS                        |
+-----------------------------------------------------------+
|  Habit: Drink Water                                       |
|  Type: Positive                                           |
|  Description: Drink 2L of water daily                     |
|  Status: Active                                           |
+-----------------------------------------------------------+
|  [Add Log Entry]                                          |
+-----------------------------------------------------------+
|  LOG HISTORY                                              |
|  -------------------------------------------------------- |
|  Date        Completed   Notes                            |
|  -------------------------------------------------------- |
|  2026-03-04  Yes         Felt good today                  |
|  2026-03-03  No          Forgot                           |
|  2026-03-02  Yes         -                                |
|                                                           |
+-----------------------------------------------------------+
```

---

## 📝 Log Entry Form
```
+-----------------------------------------------------------+
|                     ADD LOG ENTRY                         |
+-----------------------------------------------------------+
|  Habit: Drink Water                                       |
|                                                           |
|  Date: [ 2026-03-05 ]                                     |
|                                                           |
|  Completed: [✓] Yes                                       |
|                                                           |
|  Notes:                                                   |
|  -------------------------------------------------------- |
|  |                                                      | |
|  |                                                      | |
|  -------------------------------------------------------- |
|                                                           |
|  [ Save Log Entry ]                                       |
+-----------------------------------------------------------+
```

---

## ➕ Add Habit Form
```
+-----------------------------------------------------------+
|                        ADD HABIT                          |
+-----------------------------------------------------------+
|  Name: [________________________]                         |
|                                                           |
|  Description:                                             |
|  -------------------------------------------------------- |
|  |                                                      | |
|  |                                                      | |
|  -------------------------------------------------------- |
|                                                           |
|  Habit Type: ( ) Positive   ( ) Negative                 |
|                                                           |
|  [ Create Habit ]                                         |
+-----------------------------------------------------------+
```

---

## 📄 Habit Detail Page
```
+-----------------------------------------------------------+
|                      HABIT DETAILS                        |
+-----------------------------------------------------------+
|  Habit: Drink Water                                       |
|  Type: Positive                                           |
|  Description: Drink 2L of water daily                     |
|  Status: Active                                           |
+-----------------------------------------------------------+
|  [Add Log Entry]                                          |
+-----------------------------------------------------------+
|  LOG HISTORY                                              |
|  -------------------------------------------------------- |
|  Date        Completed   Notes                            |
|  -------------------------------------------------------- |
|  2026-03-04  Yes         Felt good today                  |
|  2026-03-03  No          Forgot                           |
|  2026-03-02  Yes         -                                |
|                                                           |
+-----------------------------------------------------------+
```

---

These wireframes provide a clear visual guide for how users will navigate HabitFlow and interact with its core features. They outline the structure of each key page before any front‑end development begins, ensuring that the user experience is planned intentionally and aligns with the underlying data model. With these layouts established, the next step is to implement the Habit and LogEntry functionality in the UI, beginning with CRUD operations and dashboard interactions.

---

# 🧱 Data Model

## 👤 User & Profile

Django’s User model handles authentication.  
A Profile extends it with:

- `role` — `"user"` or `"admin"`

A signal automatically creates a Profile when a User is created.

### User ↔ Profile Diagram

```
+------------------+        1 : 1        +----------------------+
|     User         |-------------------->|       Profile        |
+------------------+                     +----------------------+
| id               |                     | id                   |
| username         |                     | user_id (FK)         |
| password         |                     | role                 |
| email            |                     +----------------------+
+------------------+
```

---

## 🌱 Habit Model

Represents a behaviour the user wants to track.

Key fields:

- `name`  
- `description`  
- `habit_type` — `"positive"` or `"negative"`  
- `is_active`  
- `user` (FK)  
- Unique constraint: one habit name per user  

---

## 📅 LogEntry Model

Represents a single day’s progress for a habit.

Key fields:

- `habit` (FK)  
- `date`  
- `completed`  
- `notes`  
- Unique constraint: one log per habit per date  

### Behaviour Logic

- Positive habits → `completed=True` means *did the habit*  
- Negative habits → `completed=True` means *avoided the habit*  

---

## 🗺️ ERD Diagram

### Relationships

- User → Profile (1:1)  
- User → Habit (1:M)  
- Habit → LogEntry (1:M)  

### Relationship Table

| Model    | Relationship | Target     | Cardinality | Notes |
|----------|-------------|------------|-------------|-------|
| User     | has one     | Profile    | 1 → 1       | Auto‑created |
| User     | has many    | Habit      | 1 → many    | Each habit belongs to a user |
| Habit    | has many    | LogEntry   | 1 → many    | One log per date |
| LogEntry | belongs to  | Habit      | many → 1    | Cascade delete |
| Profile  | belongs to  | User       | 1 → 1       | Extends user |

---

# 🛠 Project Setup

- Virtual environment created  
- Django installed  
- Project created (`habitflow`)  
- Main app created (`tracker`)  
- Requirements file generated  
- GitHub repo + project board created  
- Templates and static directories configured  

---

# 📅 Development Log

## Day 1 — Project Foundation
- Created Django project and core app  
- Set up templates and static directories  
- Implemented base template with Bootstrap  
- Added homepage  
- Initial migrations completed  

## Day 2 — Authentication & Profile System
- Registration, login, logout  
- Bootstrap‑styled forms  
- Django messages  
- Dynamic navbar  
- Profile model + auto‑create signal  
- Admin‑only navigation  
- Profile moved to `accounts` for cleaner architecture  

## Day 3 — Database Schema & Models
- Habit model  
- LogEntry model  
- Unique constraints  
- Admin registration  
- ERD diagram  
- README updates  

## Day 4 — Habit CRUD Functionality
- Full CRUD for habits  
- Access control via `get_queryset()`  
- Success messages  
- Habit Detail page implemented  

## Day 5 — Logging System
- LogEntry CRUD (create, edit, delete)  
- Integrated logs into Habit Detail page  
- Date filtering  
- Validation for future dates + duplicates  
- Polished templates  
- README updated  

---

### Overview
Today focused on implementing full CRUD (Create, Read, Update, Delete) functionality for user habits. All habit operations are now fully functional, secure, and restricted to authenticated users only. This ensures that each user can manage their own habits without accessing or modifying data belonging to others.


### Habit CRUD Features

#### ✔ Create Habits
Users can create new habits using a dedicated form. Each habit is automatically assigned to the logged‑in user, ensuring correct ownership.

#### ✔ Read Habits
The Habit List page displays all active habits belonging to the current user. A Habit Detail page provides additional information and links to edit or delete the habit.

#### ✔ Update Habits
Users can edit their existing habits using the same form template used for creation. A success message confirms the update.

#### ✔ Delete Habits
Users can delete habits through a confirmation page. A success message confirms the deletion, and the user is redirected back to the Habit List.


### Access Control & Security

To ensure users can only view or modify their own habits, each class‑based view overrides `get_queryset()`:

```python
def get_queryset(self):
    return Habit.objects.filter(user=self.request.user)
```
---

# 📚 Documentation

Stored in `/docs`:

- HabitFlow Project Timeline  
- HabitFlow Marking Criteria  

---

# 🧰 Tech Stack

- Django  
- HTML, CSS, JavaScript  
- Bootstrap  
- PostgreSQL (Heroku)  
- Git & GitHub  

---

# 🔐 Security Notes

During development, the Django `SECRET_KEY` is stored in `settings.py`.  
Before deployment, it will be moved to environment variables using:

- `env.py` locally  
- Heroku config vars in production  

