# HabitFlow

HabitFlow is a full-stack Django web application designed to help users build, track, and maintain positive habits through daily logging, streaks, and progress insights.

## Project Overview
HabitFlow enables users to create habits, log daily progress, and view streaks and completion history. The project is built using Django, HTML, CSS, and JavaScript, and follows Agile methodology throughout development.

## Agile Planning

This project follows an Agile methodology using GitHub Projects to manage user stories, tasks, and development progress. A Kanban-style board is used to track work through the stages: *To Do*, *In Progress*, *In Review*, and *Done*.

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
