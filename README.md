# HabitFlow

HabitFlow is a full-stack Django web application designed to help users build, track, and maintain positive habits through daily logging, streaks, and progress insights.

## Project Overview

HabitFlow enables users to create habits, log daily progress, and view streaks and completion history. The project is built using Django, HTML, CSS, and JavaScript, and follows Agile methodology throughout development.

## Agile Planning

This project follows an Agile methodology using GitHub Projects to manage user stories, tasks, and development progress. A Kanban-style board is used to track work through the stages: _To Do_, _In Progress_, _In Review_, and _Done_.

**Project Board:**  
[View the HabitFlow Project Board](https://github.com/users/thejog2/projects/7)

---

## User Stories

### Authentication

- **US01:** As a new user, I want to register an account so I can track my habits.
- **US02:** As a returning user, I want to log in so I can access my habits.
- **US03:** As a user, I want to log out so my account stays secure.

### Habit Management

- **US04:** As a user, I want to create habits so I can track them daily.
- **US05:** As a user, I want to edit my habits so I can update their details.
- **US06:** As a user, I want to delete habits I no longer track.

### Daily Logging

- **US07:** As a user, I want to log daily habit completion so I can track progress.
- **US08:** As a user, I want to view my log history so I can see past performance.

### Dashboard

- **US09:** As a user, I want to view today’s habits so I know what to complete.
- **US10:** As a user, I want to see streaks so I stay motivated.

### UX & Accessibility

- **US11:** As a user, I want the site to be responsive so I can use it on any device.
- **US12:** As a user with accessibility needs, I want the site to be usable with assistive tools.

### Deployment

- **US13:** As a developer, I want to deploy the project so users can access it online.

---

## Task Management

Each user story is broken down into smaller development tasks on the project board. Tasks move through the workflow:

- **To Do** → **In Progress** → **In Review** → **Done**

This ensures clear visibility of progress and supports iterative development throughout the project.

## Project Setup

The project was initialised using Django within a dedicated virtual environment.  
The following steps were completed during initial setup:

- Virtual environment created and activated
- Django installed via pip
- Django project created (`habitflow`)
- Main application created (`tracker`)
- Requirements file generated (`pip freeze > requirements.txt`)
- Repository structure organised and committed to GitHub
- GitHub Project board created and linked to the repository

## Day 1: Project Foundation

Day 1 focused on establishing a clean, scalable foundation for the application. This included setting up the Django environment, structuring the project, configuring templates and static files, and implementing a responsive front‑end framework.

### Key Achievements

- Created Django project (`habitflow`) and core application (`tracker`)
- Set up a dedicated `templates/` directory at the project root
- Added a global `static/` directory for front‑end assets
- Implemented a base template with:
  - Bootstrap 5 for layout and responsiveness
  - A reusable navigation bar
  - A message display area for Django’s messaging framework
  - A central content block for page‑specific templates
- Created and rendered the homepage (`home.html`)
- Configured static file handling (`STATIC_URL` and `STATICFILES_DIRS`)
- Verified the full request → view → template pipeline
- Applied initial migrations to prepare the database
- Committed the full Day 1 foundation to version control

### Project Structure (as of Day 1)

```
habitflow/
│
├── habitflow/              # Project configuration and settings
├── tracker/                # Main application
├── templates/              # Global HTML templates
│     ├── base.html
│     └── home.html
├── static/                 # Static assets (CSS, JS, images)
│     └── css/
│          └── style.css
├── manage.py
└── requirements.txt
```

## Day 2 – User Authentication & Profile System

### Overview
Day 2 established HabitFlow’s full authentication flow and introduced the Profile model, which extends Django’s built‑in User model. Together, these features allow users to register, log in, log out, and have personalised data stored through a one‑to‑one Profile relationship. This forms the foundation for dashboards, habit tracking, and role‑based access.

---

## Core Features Completed

### 1. Registration (US01)
Users can create an account through a Bootstrap‑styled registration form. Successful registration logs the user in automatically and redirects them to the homepage with a confirmation message.

**Key elements:**
- `/register/` route  
- `UserCreationForm`  
- Automatic login  
- Success/error messages  

---

### 2. Login (US02)
Returning users authenticate through a secure login form.

**Key elements:**
- `/login/` route  
- `AuthenticationForm`  
- Session creation  
- Success/error messages  

---

### 3. Logout (US03)
Users can end their session cleanly and return to the homepage.

**Key elements:**
- `/logout/` route  
- Django’s `logout()`  
- Success message  

---

### 4. Dynamic Navbar
The navbar now adapts based on authentication state:

- **Logged out:** Login | Register  
- **Logged in:** Dashboard | Logout  
- **Admin users:** Dashboard | Admin Dashboard | Logout  

This improves navigation clarity and prepares the UI for future habit‑tracking features.

---

## Profile Model & Role System

### Why the Profile model was added
Django’s User model handles authentication but not app‑specific data. HabitFlow needs a place to store user roles and future personalisation settings. The Profile model provides this through a one‑to‑one relationship with User.

### What the Profile model includes
- `user` — One‑to‑one link to Django User  
- `role` — `"user"` or `"admin"`  

### Automatic profile creation
A Django signal ensures every new user automatically receives a Profile, guaranteeing `user.profile` always exists.

---

## User ↔ Profile Relationship Diagram

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

This structure keeps authentication clean while allowing HabitFlow to grow with user‑specific features.

---

## Role‑Based Access

HabitFlow uses a simple but scalable role system to control access to admin‑level features. While Django provides built‑in permissions (`is_staff`, `is_superuser`), the application requires its own role field to support future customisation and user‑specific behaviour. This is handled through the Profile model.

### How roles work
Each user has an associated Profile with a `role` field. The available roles are:
- `"user"` — standard application access  
- `"admin"` — elevated access to administrative tools  

Roles are stored in the database and can be managed through Django’s admin interface.

### How roles affect the UI
The navigation bar adapts based on the user’s role:
- Standard users see: **Dashboard | Logout**
- Admin users see: **Dashboard | Admin Dashboard | Logout**

The Admin Dashboard link appears only when:

user.is_authenticated and user.profile.role == "admin"


This ensures that administrative tools are visible only to authorised users.

### Automatic profile creation
A Django `post_save` signal ensures every new user automatically receives a Profile. This guarantees that `user.profile` always exists, allowing role checks to be performed safely throughout the application.

### Why this approach was chosen
Using a Profile‑based role system provides:
- A clear separation between authentication (User) and application‑specific data (Profile)
- Flexibility to add more roles or permissions in future
- A consistent way to manage user‑level behaviour across the project

This structure prepares HabitFlow for future enhancements such as analytics, moderation tools, or custom admin dashboards.


---

## Profile Signal Flow

```mermaid
flowchart TD
    A[User Created] --> B[Django post_save Signal Fired]
    B --> C[Profile.objects.create(user=user)]
    C --> D[Profile Automatically Linked to User]
```
---

## Technical Summary
- Implemented registration, login, and logout using Django’s authentication system  
- Added Bootstrap‑styled templates for all auth pages  
- Integrated Django messages for user feedback  
- Created Profile model with role field  
- Added signals to auto‑create profiles  
- Added admin‑only navigation using `user.profile.role`  
- Updated navbar to maintain consistent button positions  

---

## Status at End of Day 2
HabitFlow now has a complete authentication system and a scalable user‑profile architecture. This unlocks all user‑specific features planned for Day 3, including habit creation, dashboards, and personalised data handling.


### Front‑End Framework

Bootstrap 5 is integrated via CDN to provide a modern, responsive UI from the outset. A custom `style.css` file is included for future overrides and branding, allowing HabitFlow to develop its own visual identity while retaining Bootstrap’s flexibility.

## Documentation

Additional planning and assessment documents are stored in the `/docs` folder:

- [Habitflow Project Timeline](docs/Habitflow%20Project%20Timeline.docx)
- [Habitflow Project Marking Criteria](docs/Habitflow%20Project%20Marking%20Criteria.docx)

More documentation will be added as the project progresses.

## Tech Stack

- Django (Python)
- HTML5, CSS3, JavaScript
- Bootstrap (optional)
- PostgreSQL (Heroku)
- Git & GitHub
- Heroku for deployment

### Security Notes

During development, the Django SECRET_KEY is stored in settings.py.  
Before deployment, this will be moved to environment variables using an env.py file and Heroku config vars.
