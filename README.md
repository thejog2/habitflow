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
