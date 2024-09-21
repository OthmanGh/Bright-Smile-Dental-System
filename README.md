# Bright Smile Dental Management Platform

This is a web-based management platform for **Bright Smile Dental Systems**. The platform allows administrative users to manage clinics, doctors, and patients, as well as schedule appointments and track visits.

## Features

- **User Authentication**: Admin users can log in using an email and password (Django's built-in authentication).

- **Clinics Management**:

- View a list of clinics with key information (name, phone, location, number of doctors and patients).

- Edit clinic details and manage doctor affiliations.

- **Doctors Management**:

- View a list of doctors with key information (NPI, name, specialties, clinics, and patient affiliations).

- Edit doctor details, including specialties and contact information.

- **Patients Management**:

- View a list of patients with details on their visits and appointments.

- Edit patient information and manage visits and appointments.

- **Scheduling Appointments**:

- Schedule patient appointments by selecting available doctors, clinics, and procedures.

## Tech Stack

- **Backend**: Django 5.1.1 (also used for the frontend via Django templates)

- **Frontend**: HTML, Bootstrap, and JavaScript

- **Database**: PostgreSQL

- **REST API**: Django REST framework for external API access

## Setup Instructions

### Prerequisites

- Python 3.8+

- PostgreSQL

- Git

### Installation

1\. Clone the repository:

```

git clone https://github.com/OthmanGh/Bright-Smile-Dental-System.git

cd Bright-Smile-Dental-System

```

2\. Create a virtual environment and activate it:

```

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

3\. Install required packages:

```

pip install -r requirements.txt

```

### Environment Variables

Create a `.env` file at the root of your project to store environment variables:

```ini

DB_NAME=<your_db_name>

DB_USER=<your_db_user>

DB_PASSWORD=<your_db_password>

DB_HOST=localhost

DB_PORT=5432

SECRET_KEY=<your_secret_key>

DEBUG=True

```

### Database Setup

1\. Create a PostgreSQL database with the name specified in your `.env` file.

2\. Apply migrations:

```

python manage.py migrate

```

3\. (Optional) Load initial data:

```

python manage.py loaddata initial_data

```

### Running the Application

1\. Start the development server:

```

python manage.py runserver

```

2\. Access the application at `http://127.0.0.1:8000/`

## REST API Endpoints

The following REST API endpoints are available for external systems:

- Add Patient: `POST http://127.0.0.1:8000/api/patients/`

- Add Doctor: `POST http://127.0.0.1:8000/api/doctors/`

- Add Clinic: `POST http://127.0.0.1:8000/api/clinics/`

- Get Clinic Information: `GET http://127.0.0.1:8000/api/clinics/{id}/`
