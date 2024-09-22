Bright Smile Dental Management Platform
=======================================

This is a web-based management platform for **Bright Smile Dental Systems**. The platform allows administrative users to manage clinics, doctors, and patients, as well as schedule appointments and track visits.

Features
--------

-   **User Authentication**: Admin users can log in using an email and password (Django's built-in authentication).
-   **Clinics Management**:
    -   View a list of clinics with key information (name, phone, location, number of doctors and patients).
    -   Edit clinic details and manage doctor affiliations.
-   **Doctors Management**:
    -   View a list of doctors with key information (NPI, name, specialties, clinics, and patient affiliations).
    -   Edit doctor details, including specialties and contact information.
-   **Patients Management**:
    -   View a list of patients with details on their visits and appointments.
    -   Edit patient information and manage visits and appointments.
-   **Scheduling Appointments**:
    -   Schedule patient appointments by selecting available doctors, clinics, and procedures.

Tech Stack
----------

-   **Backend**: Django 5.1.1 (also used for the frontend via Django templates)
-   **Frontend**: HTML, Bootstrap, and JavaScript
-   **Database**: PostgreSQL
-   **REST API**: Django REST framework for external API access

Setup Instructions
------------------

### Prerequisites

-   Python 3.8+
-   PostgreSQL
-   Git

### Installation

1.  Clone the repository:

`git clone https://github.com/OthmanGh/Bright-Smile-Dental-System.git
cd Bright-Smile-Dental-System`

1.  Create a virtual environment and activate it:

`python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate``

1.  Install required packages:

`pip install -r requirements.txt`

### Environment Variables

Create a `.env` file at the root of your project to store environment variables:

`DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=<your_secret_key>
DEBUG=True`

### Database Setup

1.  Create a PostgreSQL database with the name specified in your `.env` file.
2.  Apply migrations:


`python manage.py migrate`

1.  (Optional) Load initial data:


`python manage.py loaddata initial_data`

### Creating a Superuser

To access the admin interface and create initial users, you need to create a superuser:


`python manage.py createsuperuser`

Follow the prompts to set up your superuser account. You can then use these credentials to log in to the admin interface at `http://127.0.0.1:8000/admin/` and create additional users.

### Running the Application

1.  Start the development server:

`python manage.py runserver`

1.  Access the application at `http://127.0.0.1:8000/`

REST API Endpoints
------------------

The following REST API endpoints are available for external systems:

-   Add Patient: `POST http://127.0.0.1:8000/api/patients/`
-   Add Doctor: `POST http://127.0.0.1:8000/api/doctors/`
-   Add Clinic: `POST http://127.0.0.1:8000/api/clinics/`
-   Get Clinic Information: `GET http://127.0.0.1:8000/api/clinics/{id}/`

### API Usage Examples

To use these APIs, you can use tools like cURL or Postman. Here are some examples:

1.  Add a new patient:


`curl -X POST http://127.0.0.1:8000/api/patients/
-H "Content-Type: application/json"
-d '{
    "name": "Liam Fletcher",
    "date_of_birth": "1995-09-30",
    "address": "123 Zahle St",
    "phone_number": "452-655-7426",
    "last_4_ssn": "5724",
    "gender": "Male"
}'`

1.  Get clinic information:

`curl http://127.0.0.1:8000/api/clinics/1/`

Running Tests
-------------

To run the unit tests:

`python manage.py test`

Deployment
----------

The application is deployed and accessible at: <https://bright-smile.onrender.com/>

You can visit this link to see the actual working application.

Assumptions and Limitations
---------------------------

-   The platform assumes a single time zone for all operations. Future versions may need to handle multiple time zones for different clinic locations.
-   Patient data is simplified and does not include comprehensive medical history or insurance information.

Future Enhancements
-------------------

1.  **Search and Filter Features**: Implement advanced search and filtering options for clinics, doctors, and patients to improve navigation and data retrieval.
2.  **Patient Portal**: Develop a separate interface for patients to view their appointments, medical history, and request appointments.
3.  **Notification System**: Implement email or SMS notifications for appointment reminders and important updates.

These enhancements would significantly improve the functionality and user experience of the Bright Smile Dental Management Platform.
