# 📘 HabitFlow — Habit Tracking Web Application

HabitFlow is a full‑stack Django web application designed to help users build, track, and maintain both positive and negative habits through daily logging, streaks, and progress insights. The project follows Agile methodology and is developed iteratively over a multi‑day sprint.

---

# 📑 Table of Contents

1. Project Overview  
2. Agile Planning  
3. User Stories & Acceptance Criteria  
4. Features  
5. Wireframes  
6. Data Model & ERD  
7. Project Setup  
8. Development Log  
9. Screenshots (Placeholder)  
10. Testing (Placeholder)  
11. Deployment (Placeholder)  
12. AI Usage Reflection (Placeholder)  
13. Tech Stack  
14. Security Notes  

---

# 📘 Project Overview

HabitFlow enables users to:

- Create habits  
- Track daily progress  
- Log completions or avoidance  
- View streaks and history  
- Maintain both positive and negative habits  
- Access a personalised dashboard  
- (Admins only) View platform‑wide analytics  

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

Daily development logs (below) document progress and decisions.

---

# 🧑‍💻 User Stories & Acceptance Criteria

### Authentication
- **US01:** Register an account  
- **US02:** Log in  
- **US03:** Log out  

### Habit Management
- **US04:** Create habits  
- **US05:** Edit habits  
- **US06:** Delete habits  

### Daily Logging
- **US07:** Log daily progress  
- **US08:** View log history  

### Dashboard
- **US09:** View today’s habits  
- **US10:** View streaks  

### UX & Accessibility
- **US11:** Responsive design  
- **US12:** Accessibility support  

### Deployment
- **US13:** Deploy the project  

(Full acceptance criteria will be added during the testing phase.)

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

### ✔ Dashboard  
Displays today’s habits, streaks, and quick‑log buttons.

### ✔ Admin Tools  
Superusers can access a custom Admin Dashboard with platform‑wide analytics.

### ✔ Responsive UI  
Bootstrap‑powered layout with custom CSS.

### ✔ Accessibility  
Semantic HTML, ARIA labels, WCAG‑compliant contrast, and keyboard‑friendly navigation.

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
**Focus:** Establishing the core structure of the Django project.

### Key Work Completed
- Created the Django project and initial `tracker` app  
- Set up global templates and static directories  
- Implemented the base template with Bootstrap  
- Added the homepage and navigation structure  
- Ran initial migrations and confirmed project bootstrapping  

### Outcome
A clean, well‑structured foundation was established, ensuring all future development could build on a stable and organised project layout.

---

## Day 2 — Authentication & Profile System
**Focus:** Implementing user authentication and extending user data.

### Key Work Completed
- Added registration, login, and logout functionality  
- Styled authentication forms using Bootstrap  
- Integrated Django messages for user feedback  
- Added dynamic navbar elements based on authentication state  
- Created a Profile model with automatic creation via signals  
- Moved profile logic into a dedicated `accounts` app for cleaner architecture  
- Added admin‑only navigation options  

### Outcome
Users can now securely register and authenticate, and the system supports role‑based behaviour through the Profile model.

---

## Day 3 — Database Schema & Models
**Focus:** Designing and implementing the core data models.

### Key Work Completed
- Implemented the `Habit` model with unique constraints  
- Implemented the `LogEntry` model with per‑day uniqueness  
- Registered both models in Django admin  
- Created the ERD diagram to document relationships  
- Updated the README with schema details  

### Outcome
The project now has a complete, well‑structured data model ready for CRUD functionality and dashboard logic.

---

## Day 4 — Habit CRUD Functionality
**Focus:** Allowing users to manage their habits.

### Key Work Completed
- Implemented full CRUD operations for habits  
- Added access control using `get_queryset()` to ensure users only manage their own habits  
- Added success messages for create/update/delete actions  
- Built the Habit Detail page to display habit information  

### Outcome
Users can now create, view, edit, and delete habits, forming the backbone of the habit‑tracking workflow.

---

## Day 5 — Logging System
**Focus:** Enabling users to record daily progress.

### Key Work Completed
- Implemented CRUD operations for LogEntry  
- Integrated logs into the Habit Detail page  
- Added validation for duplicate logs and future dates  
- Improved template structure and styling  
- Updated README with logging documentation  

### Outcome
Users can now record daily progress for each habit, forming the basis for streaks and dashboard insights.

---

## Day 6 — Dashboard & Streak Logic
**Focus:** Transforming HabitFlow into a daily‑driven habit‑tracking experience.

### Key Work Completed
- Built the Dashboard view and template  
- Added quick‑log buttons for one‑click daily tracking  
- Implemented streak calculation logic for both positive and negative habits  
- Added helper functions (`has_logged_today`, `get_today_log`, `calculate_streak`)  
- Updated navbar to include Dashboard access  
- Ensured all dashboard features require authentication  

### Outcome
The Dashboard became the central user experience, enabling fast daily logging and providing meaningful streak insights.

---

## Day 7 — UI/UX Polish, Branding, Accessibility & Documentation
**Focus:** Refining the interface and improving accessibility.

### Key Work Completed
- Performed a full UI/UX pass across all pages  
- Consolidated and cleaned CSS for maintainability  
- Improved form layouts, spacing, and visual hierarchy  
- Enhanced responsive behaviour across mobile and tablet  
- Added a custom favicon and strengthened branding  
- Improved accessibility (ARIA labels, semantic HTML, WCAG contrast)  
- Ran Lighthouse and WAVE audits and resolved issues  
- Expanded README with UX design, wireframes, palette, and accessibility notes  

### Outcome
HabitFlow now feels cohesive, polished, and accessible, with a strong visual identity and improved documentation.

---

## Day 8 — Admin Dashboard, Navbar Fixes & Structural Enhancements
**Focus:** Adding internal admin tools and fixing mobile navigation.

### Key Work Completed
- Fixed mobile/tablet navbar visibility issues  
- Created a dedicated `adminpanel` app  
- Built a custom Admin Dashboard for superusers  
- Added system‑level analytics (users, habits, logs, averages)  
- Added a user overview table with activity metrics  
- Ensured admin‑only access using decorators  
- Integrated the dashboard into the navbar  
- Improved project structure by isolating admin logic  

### Outcome
HabitFlow now includes a secure, branded Admin Dashboard that provides assessors and superusers with clear insights into platform activity.

---

## Day 9 — Documentation, Screenshots & Project Board Updates
**Focus:** Strengthening documentation and preparing for testing week.

### Key Work Completed
- Expanded README with user stories, wireframes, ERD, features, and future enhancements  
- Added placeholders for screenshots, testing, deployment, and AI reflection  
- Updated GitHub Project Board and moved documentation tasks to **Done**  
- Prepared structure for upcoming testing week  

### Outcome
Documentation is now comprehensive and structured, setting the stage for final testing, deployment, and assessor‑ready presentation.

---

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

