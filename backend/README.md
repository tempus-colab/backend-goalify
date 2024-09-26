Goalify - Backend

Overview

Goalify is a backend system built with Flask and MySQL for managing goals and tasks. It allows users to create, update, delete goals, and manage tasks associated with those goals.

Technologies Used

Flask: Web framework for the API
SQLAlchemy: ORM for database interaction
MySQL: Database for storing data

Prerequisites

Python 3.x
MySQL Server
Postman/Insomnia for API testing

Setup

1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/goalify-backend.git
cd goalify-backend
2. Create a Virtual Environment and Install Dependencies
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Set Up MySQL Database
Create a MySQL database:
sql
Copy code
CREATE DATABASE goalify;
Update config.py with your MySQL credentials:
python
Copy code
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<username>:<password>@localhost/goalify'
4. Apply SQL Tables Manually

Run these SQL queries in MySQL Workbench or MySQL CLI to create the tables:

sql
Copy code
CREATE TABLE goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    reminder_time TIME
);

CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    goal_id INT,
    task_description TEXT NOT NULL,
    due_date DATE,
    status VARCHAR(100) DEFAULT 'pending',
    FOREIGN KEY (goal_id) REFERENCES goals(goal_id)
);
5. Run the Flask App
bash
Copy code
flask run
The app will be running on http://127.0.0.1:5000.

API Endpoints
1. Get All Goals
URL: /goals
Method: GET
2. Add a New Goal
URL: /goals
Method: POST
Body (JSON):
json
Copy code
{
  "title": "Complete Backend",
  "description": "Create the backend system",
  "start_date": "2024-09-26",
  "end_date": "2024-10-01",
  "reminder_time": "08:30:00"
}
3. Update a Goal
URL: /goals/<goal_id>
Method: PUT
4. Delete a Goal
URL: /goals/<goal_id>
Method: DELETE
5. Get All Tasks for a Goal
URL: /goals/<goal_id>/tasks
Method: GET
6. Add a Task to a Goal
URL: /goals/<goal_id>/tasks
Method: POST
7. Update a Task
URL: /goals/<goal_id>/tasks/<task_id>
Method: PUT
8. Delete a Task
URL: /goals/<goal_id>/tasks/<task_id>
Method: DELETE
