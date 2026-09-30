# Job Application Tracker

A multi-user web application built with Django that helps users organize, track, and manage their job applications from one dashboard.

## Features

- User registration and login
- Secure user-specific application tracking
- Add, edit, view, and delete job applications
- Application status tracking
- Job type classification
- Priority levels
- Application and interview dates
- Follow-up dates
- Contact person information
- Salary information
- Job posting URLs
- Application and interview notes
- Search applications by company or job title
- Filter applications by status
- Sort applications
- Dashboard statistics
- Pagination
- User profile
- Password change functionality
- Responsive interface

## Application Statuses

The application supports the following statuses:

- Saved
- Applied
- Interview
- Assessment
- Rejected
- Offer

## Job Types

- Full-time
- Part-time
- Internship
- Contract
- Freelance
- Remote
- Hybrid

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- Django Templates
- Git & GitHub

## Project Structure

```text
job-application-tracker/
│
├── accounts/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── applications/
│   ├── migrations/
│   ├── templates/
│   │   └── applications/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── accounts/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md