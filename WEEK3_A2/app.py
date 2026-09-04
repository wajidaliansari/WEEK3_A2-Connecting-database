from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_FILE = 'tasks.db'

# ==================
# DATABASE SETUP
# ==================
def init_database():
    """Create database and table if they don't exist"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN DEFAULT 0
        )
    ''')
    
    # Insert example tasks only if table is empty
    cursor.execute('SELECT COUNT(*) FROM tasks')
    count = cursor.fetchone()[0]
    
    if count == 0:
        cursor.execute('INSERT INTO tasks (title, done) VALUES (?, ?)', ('Buy milk', 0))
        cursor.execute('INSERT INTO tasks (title, done) VALUES (?, ?)', ('Learn SQLite', 0))
        cursor.execute('INSERT INTO tasks (title, done) VALUES (?, ?)', ('Build an API', 0))
    
    conn.commit()
    conn.close()

# Initialize database when app starts
init_database()

# ==================
# HELPER FUNCTION
# ==================
def get_db_connection():
    """Connect to database and return connection"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

# ==================
# GET - Read all tasks
# ==================
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    
    # Convert rows to dictionaries
    return jsonify([dict(task) for task in tasks])

# ==================
# GET - Read one task
# ==================
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify(dict(task))

# ==================
# POST - Create task
# ==================
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    # Validate
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    title = data['title']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, done) VALUES (?, ?)', (title, 0))
    conn.commit()
    
    task_id = cursor.lastrowid
    conn.close()
    
    return jsonify({
        'id': task_id,
        'title': title,
        'done': 0
    }), 201

# ==================
# PUT - Update task
# ==================
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    
    # Check if task exists
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    
    if task is None:
        conn.close()
        return jsonify({'error': 'Task not found'}), 404
    
    # Get current values
    title = data.get('title', task['title'])
    done = data.get('done', task['done'])
    
    # Update
    cursor.execute('UPDATE tasks SET title = ?, done = ? WHERE id = ?', (title, done, task_id))
    conn.commit()
    conn.close()
    
    return jsonify({
        'id': task_id,
        'title': title,
        'done': done
    })

# ==================
# DELETE - Delete task
# ==================
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Check if task exists
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    
    if task is None:
        conn.close()
        return jsonify({'error': 'Task not found'}), 404
    
    # Delete
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Task deleted'})

# ==================
# START SERVER
# ==================
if __name__ == '__main__':
    print('✅ Server running at http://localhost:5000')
    print('📁 Database: tasks.db')
    app.run(debug=True, port=5000)