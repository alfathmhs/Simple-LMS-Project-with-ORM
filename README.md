# Simple LMS Project with ORM

This project is a Learning Management System (LMS) built using Django ORM, PostgreSQL as the database, and Docker for containerization. The LMS includes basic views for managing courses, user profiles, and course statistics. Django Silk is integrated for monitoring and profiling performance.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Endpoints](#endpoints)

## Overview

This LMS allows users to:
- List all courses and their associated teachers
- View a user’s profile and the courses they teach
- Retrieve course statistics, including the number of courses, min/max/average prices, and most/least popular courses

## Features

- **Course Management**: Lists available courses and their associated teachers.
- **User Profiles**: Retrieves information about a specific user and the courses they are teaching.
- **Course Statistics**: Provides aggregate data about the courses, including min/max/average price and popularity.
- **Performance Monitoring**: Uses Django Silk for profiling to track SQL queries and optimize performance.

## Technologies

- **Django** - Web framework for Python
- **Django Silk** - For profiling and performance monitoring
- **PostgreSQL** - Database for storing LMS data
- **Docker** - For containerizing the application

## Setup and Installation

### Prerequisites

- Docker installed on your machine

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/alfathmhs/Simple-LMS-Project-with-ORM.git
   cd Simple-LMS-Project-with-ORM
   ```

2. **Build and Run Docker**
 Use Docker Compose to build and start the containers:
   ```bash
   docker compose up -d --build
   ```

3. **Apply Migrations**

    In a new terminal window, apply the migrations to set up the database tables:

- First, generate migrations
   ```bash
   docker exec simple_lms python manage.py makemigrations
   ```

- Then, apply the migrations
   ```bash
   docker exec simple_lms python manage.py migrate
   ```

4. **Restart the Docker Containers**

   After applying migrations, restart the Docker containers to ensure all changes are loaded correctly:
   ```bash
   docker compose restart
   ```

5. **Import Dummy Data**
To test the application with some dummy data, run the following command:
   ```bash
   docker exec simple_lms python importer.py
   ```

6. **(Optional) Creating a Default Superuser**

   If you need to create a default superuser to access the Django admin panel, use the following Docker command:
   ```bash
   docker exec simple_lms python manage.py createsuperuser
   ```

7. **Access the Application**
- Visit http://localhost:8081/admin to access the Django admin panel.
- Explore the API endpoints described below.
   
## Endpoints

| Endpoint                | HTTP Method | Description |
|-------------------------|-------------|-------------|
| `/courses`              | GET         | Lists all courses with their names, prices, and teacher information |
| `/course_stat`          | GET         | Displays course statistics such as course count, min/max/avg prices, and popular/unpopular courses |
| `/profile/<user_id>`    | GET         | Retrieves the profile of a specific user and their taught courses |
| `/silk/`                | GET         | Access Django Silk profiling data |