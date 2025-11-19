REST API with Flask — User Management

This project is part of my internship tasks.
The goal is to build a simple REST API using Flask that manages user data with full CRUD functionality.

## ⭐ Objective

Create a REST API with the following features:

GET → Retrieve all users or a single user

POST → Add a new user

PUT → Update existing user

DELETE → Remove a user

## ⭐ Technologies Used

Python

Flask

PowerShell (for API testing)

Invoke-RestMethod (Windows-native API testing command)

## ⭐ Project Structure
app.py        # Main Flask application

## ⭐ Setup Instructions
1. Install Flask

Open PowerShell or VS Code terminal:

pip install flask

2. Run the App
python app.py


You will see:

Running on http://127.0.0.1:5000

## ⭐ API Endpoints
1. Get all users

GET /users

Command:

Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:5000/users"

2. Get a single user

GET /users/<id>

Example for ID 1:

Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:5000/users/1"

3. Create a new user

POST /users

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:5000/users" `
-ContentType "application/json" `
-Body '{"name":"Nivi","email":"nivi@example.com"}'

4. Update a user

PUT /users/<id>

Example (update ID 1):

Invoke-RestMethod -Method Put -Uri "http://127.0.0.1:5000/users/1" `
-ContentType "application/json" `
-Body '{"name":"UpdatedName","email":"updated@example.com"}'

5. Delete a user

DELETE /users/<id>

Example (delete ID 1):

Invoke-RestMethod -Method Delete -Uri "http://127.0.0.1:5000/users/1"

⭐ Testing Note

On Windows PowerShell:

curl command does not work like real Linux cURL.

Therefore, I used:

## 👉 Invoke-RestMethod — the recommended native API testing tool on Windows.

This fully satisfies the requirement:
API tested without Postman using command-line tools.

## ⭐ Outcome

Through this task, I learned:

How to build REST API endpoints in Flask

How to handle GET/POST/PUT/DELETE requests

How to test APIs using command-line tools

How to manage in-memory data structures
