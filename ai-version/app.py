import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_FILE = 'tasks.db'

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS tasks 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      title TEXT NOT NULL, 
                      done BOOLEAN DEFAULT 0)''')
        
        # Seed only if empty
        if db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 0:
            sample_tasks = [("Buy milk", 0), ("Learn SQLite", 0), ("Build an API", 0)]
            db.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", sample_tasks)
            db.commit()

init_db()

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return jsonify([dict(ix) for ix in tasks]), 200