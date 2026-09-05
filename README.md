# WEEK3_A2-Connecting-database

This is a CRUD API for managing tasks, built with Python and Flask. This project transitions the data storage from an in-memory list to a persistent SQLite database.

## 🗄️ Database Choice
**Why SQLite?** 
SQLite was chosen because it is a lightweight, serverless database that requires zero setup. It stores the entire database in a single file, making it incredibly easy to manage while perfectly allowing our task data to survive server restarts (persistence)[cite: 1].

## 📁 Database Location
The database is stored in a file named `tasks.db` located in the root of the project[cite: 1]. 
*Note: If this file is missing when you clone the repository, it will be automatically created and populated with three example tasks the first time you start the application*[cite: 1].

## 🚀 How to Start the Project
To run this project on your local machine, open your terminal in the project folder and run the following command:

```bash
python app.py