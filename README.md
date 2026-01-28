# TaskFlow 🗂️

TaskFlow is a Python-based Command Line Task Management System that helps users create, manage, and track tasks efficiently.

It focuses on clean backend logic, modular design, and persistent storage.

---

## 🚀 Features

- Create new tasks  
- List all tasks  
- Update task status (To Do → In Progress → Completed)  
- Delete tasks  
- Persistent storage using JSON  
- Command-line interface (CLI)  
- Modular and scalable architecture  

---

## 🛠️ Tech Stack

- Python 3  
- JSON (for data storage)  
- Argparse (for CLI)  

---

## 📦 Requirements

- Python 3.9 or above  

Check version:

```bash
python --version
```

---

## ▶️ Usage

### Add Task
```bash
python cli.py add "Study DSA" --desc "Arrays"
```

### List Tasks
```bash
python cli.py list
```

### Update Status
```bash
python cli.py status 1 in_progress
```

### Delete Task
```bash
python cli.py delete 1
```

---

## 👩‍💻 Author

Pranjali Sharma
