<img width="1917" height="1078" alt="Screenshot 2026-09-05 115519" src="https://github.com/user-attachments/assets/e2fa7f0b-48b7-4778-895f-6895a7348c85" />
<img width="1917" height="1078" alt="Screenshot 2026-09-05 115214" src="https://github.com/user-attachments/assets/3385baab-b438-4223-a5e6-4189d51c3799" />
<img width="1917" height="1078" alt="Screenshot 2026-09-05 115050" src="https://github.com/user-attachments/assets/0d699903-b712-459a-a89b-76f2e9d4eda7" />
<img width="1917" height="1078" alt="Screenshot 2026-09-05 114924" src="https://github.com/user-attachments/assets/f4fe48f1-208f-4da3-b266-94928dfa69f7" />
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
