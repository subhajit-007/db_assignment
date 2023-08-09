# Python Console App to perform mongodb CRUD operations

---
# Todo Application

---

# Required packages:
1. Pymongo
2. mongodb local server

---

# How to run the application

1. Create VENV using the requirement file provided
2. Open local mongodb server and run the server
3. Copy the Database server URL and replace with the `.env` files `MONGODB_URL` value
4. Make sure all files are in the project level path
5. Run app.py using command: `$ py app.py`

---
# Assumptions

1. App has CRUD functionality with delete all feature
2. delete all remove all the data from the table
3. when run the application. make sure DB server running.
4. It will create database and collection using the config file automatically.
5. DB name will `Todo` and collection name `Tasks`
6. Each Task will be saved in the DB with the "task_name" as task and with priority as "task_priority".
7. There are three types of `task_priority`:
    * Low saved as `0` in the DB
    * Mid saved as `1` in the DB
    * High saved as `2` in the DB
8. Delete will be done by the `task_name`
9. While Chose an option in the console. use numeric values. (errors are handled here)

