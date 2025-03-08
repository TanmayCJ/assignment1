# Project Details

### Installation Guide
# Sustainability Tracker Assignment (Backend)

This repository contains the code for the backend of a sustainability tracker application, built using Django.

## Table of Contents

- [Project Overview](#project-overview)
- [Backend (Django)](#backend-django)
  - [Setup and Installation](#backend-setup-and-installation)
  - [Functionality](#backend-functionality)
  - [API Endpoints](#backend-api-endpoints)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project implements the backend for a sustainability tracker, allowing users to record and manage their sustainability actions. The backend provides a RESTful API for interacting with the data.

## Backend (Django)

### Backend Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd my_sustainability_tracker
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### Backend Functionality

The Django backend provides the following functionalities:

* **Data Model:** Defines a `SustainabilityAction` model with fields for `action`, `date`, and `points`.
* **API Endpoints:** Implements CRUD (Create, Read, Update, Delete) operations for sustainability actions through RESTful API endpoints.
* **Data Storage:** Uses a database (e.g., SQLite) to store sustainability action data.

### Backend API Endpoints

* **`GET /api/actions/`:** Retrieves a list of all sustainability actions.
* **`POST /api/actions/add/`:** Creates a new sustainability action.
    * **Request body (JSON):**
        ```json
        {
          "action": "Plant a tree",
          "date": "2023-11-01",
          "points": 10
        }
        ```
* **`PUT /api/actions/<action_id>/`:** Updates an existing sustainability action.
    * **Request body (JSON):**
        ```json
        {
          "action": "Plant two trees",
          "date": "2023-11-02",
          "points": 20
        }
        ```
* **`DELETE /api/actions/<action_id>/delete/`:** Deletes a sustainability action.

## Usage

1.  **Start the Django backend server:**

    ```bash
    cd my_sustainability_tracker
    venv\Scripts\activate #or source venv/bin/activate
    python manage.py runserver
    ```

2.  **Test the API endpoints:**

    * Use Postman or curl to test the backend API endpoints.

## Dependencies

* **Backend (Django):**
    * Django
    * sqlparse
    * asgiref
    * pytz
