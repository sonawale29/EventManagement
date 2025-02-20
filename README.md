# Event Management API

## Overview
The **Event Management API** is a RESTful service built with Django REST Framework (DRF) that allows users to create, manage, and purchase event tickets.

### Features
- **User Registration & Authentication** (JWT-based authentication)
- **Event Management** (Admin Only)
- **Ticket Purchase** (Authenticated Users Only)
- **Event Listing** (Available to both Admins and Users)
- **Role-Based Access Control**

## Installation

### 1. Clone the Repository
```sh
$ git clone https://github.com/your-repo/event-management-api.git
$ cd event-management-api
```

### 2. Create & Activate Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and set up your database credentials:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Use PostgreSQL for production
```

### 5. Apply Migrations & Create Superuser
```sh
$ python manage.py migrate
$ python manage.py createsuperuser
```

### 6. Run the Development Server
```sh
$ python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /register/` - Register a new user
- `POST /login/` - Obtain JWT token

### Event Management
- `POST /events/create/` - Create a new event (**Admin Only**)
- `GET /events/` - Fetch all events (**Admin & User**)

### Ticket Purchase
- `POST /events/{event_id}/purchase/` - Purchase tickets (**Authenticated Users Only**)

## Testing APIs with Postman
1. **Obtain JWT Token** from `/login/`
2. **Use Token** in **Authorization Header** (`Bearer <your-token>`)
3. **Test Endpoints** using Postman or Curl


