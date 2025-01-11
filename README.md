# alx-capstone
web back end / ecommerce api
# E-commerce Product API

## Project Overview
This project Implement an API to manage e-commerce platform products. The API will allow for:

- CRUD Operations for Products.
- CRUD Operations for Users.
- Search Functionality.
- Authentication and Authorization.
- Data Validation
- API Design: Django Rest Framework (DRF).

This will ensure the smooth operation of the e-commerce site back-end.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Ouss27/alx-capstone.git
   cd ecommerce_api
2. create a virtual environment and acticate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
pip install -r requirements.txt
4. Run the migrations to create the database tables:
python manage.py makemigrations
python manage.py migrate
5. create superuser
python manage.py createsuperuser
6. Run the development server:
python manage.py runserver
Access the application at http://127.0.0.1:8000/


