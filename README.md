# Hospital Management System

A Django-based hospital management application for managing doctors, departments, appointments, and a smart doctor recommendation feature.

## Project Overview

This project provides a simple hospital website where users can:

- view hospital departments
- browse doctors and their specialties
- schedule appointments
- contact the hospital
- sign up and log in
- get doctor recommendations based on entered symptoms

## Tech Stack

- Python
- Django 6.1.1
- SQLite database
- Pillow for image handling
- HTML, CSS, and Django templates

## Project Structure

```text
hospital_management_system/
├── home/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── recommendation.py
│   ├── recomandations.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── hospital_management_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── seed_clinic_data.py
├── media/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── Dockerfile
└── README.md
```

## Main Features

### Doctor and Department Pages
- View all doctors
- View all departments
- Display doctor photos and specialization details

### Booking System
- Appointment booking form
- Patient details capture for appointment requests

### Authentication
- User signup
- Login/logout support
- Protected pages for staff-like flows

### Smart Recommendation
- Users can enter symptoms
- The app matches symptoms to doctor specializations
- Returns recommended doctors based on the entered text

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd hospital_management_system
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Then open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Seed Demo Data

A sample data seeding script is included in [hospital_management_system/seed_clinic_data.py](hospital_management_system/seed_clinic_data.py).

To run it:

```bash
python manage.py shell -c "exec(open('seed_clinic_data.py').read())"
```

This populates the database with departments, doctors, and booking records.

## Image Data

Doctor profile images are stored under the media folder and can also be assigned using the image script if needed.

## Admin Panel

You can access the Django admin panel at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created earlier to log in.

## Notes

- This project is configured for development use with `DEBUG = True`.
- The app currently uses SQLite for local development.
- The recommendation feature is rule-based and uses symptom matching against doctor specializations.

## Future Improvements

- add real appointment management dashboard
- add patient and doctor authentication roles
- add admin approval for bookings
- connect to a production database
- improve recommendation logic with ML or better keyword matching

## License

This project is for educational/demo purposes.
 