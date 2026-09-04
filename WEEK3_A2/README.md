# Tasks API with SQLite Database

## Project Overview
A REST API for managing tasks with SQLite database persistence.

## Why SQLite?
- Lightweight, no server needed
- Data stored in single file
- Perfect for learning backend development

## Setup & Installation

1. Clone this repository
2. Create virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Start the server:
```bash
   python app.py
```

5. Server runs at: `http://localhost:5000`

## Database
- **Location:** `tasks.db`
- **Automatically created** on first run

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/<id>` | Get one task |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

### Example Requests

**Create a task:**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'
```

**Get all tasks:**
```bash
curl http://localhost:5000/tasks
```

**Update task:**
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

## Example SQL Query
```sql
SELECT * FROM tasks WHERE done = 0;
```

## Database Screenshot
[Screenshot of DB Browser showing tasks table]