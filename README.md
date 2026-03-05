# 📘 HabitFlow — Habit Tracking Web Application

HabitFlow is a full‑stack Django web application designed to help users build, track, and maintain both positive and negative habits through daily logging, streaks, and progress insights. The project follows Agile methodology and is developed iteratively over a 7‑day sprint.

---

# 📑 Table of Contents

1. Project Overview  
2. Agile Planning  
3. User Stories  
4. Features  
5. Data Model  
   - User & Profile  
   - Habit  
   - LogEntry  
   - ERD Diagram  
6. Project Setup  
7. Development Log  
   - Day 1  
   - Day 2  
   - Day 3  
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

HabitFlow is developed using Agile methodology with a Kanban‑style GitHub Project Board.

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

This section summarises daily progress without overwhelming the main README.

---

## Day 1 — Project Foundation

- Created Django project and core app  
- Set up templates and static directories  
- Implemented base template with Bootstrap  
- Added homepage  
- Verified routing and template rendering  
- Initial migrations completed  

---

## Day 2 — Authentication & Profile System

### Completed

- Registration, login, logout  
- Bootstrap‑styled forms  
- Django messages  
- Dynamic navbar  
- Profile model with role field  
- Auto‑create Profile signal  
- Admin‑only navigation  

### Profile Refactor (Important)

Originally, Profile was inside `tracker`.  
It was moved to `accounts` to maintain a clean separation:

- `accounts` → authentication + profiles  
- `tracker` → habits + logs  

This improves maintainability and aligns with Django best practices.

---

## Day 3 — Database Schema & Models

### Completed

- Habit model  
- LogEntry model  
- Positive/negative habit support  
- Unique constraints  
- Admin registration  
- ERD diagram  
- README updates  
- Architecture refinement (Profile moved to accounts)  

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

