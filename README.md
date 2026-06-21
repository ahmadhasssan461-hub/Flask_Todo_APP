# ✅ Flask To Do List App

## 📌 About
This is a Flask web application that implements CRUD operations (Create, Read, Update, Delete). You can add tasks, view them, edit them, and delete them — all data is permanently saved in the database. 


---

## 🎯 Features
- ✅ Add tasks (Title, Date, Priority)
- ✅ View all tasks in a list
- ✅ Update/Edit tasks
- ✅ Delete tasks
- ✅ Permanently save data in SQLite Database

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite (Flask-SQLAlchemy)
- **Frontend:** HTML, Bootstrap 5
- **Templating:** Jinja2

---

## 📁 Project Structure
```
Flask-Todo-App/
├── main.py
├── templates/
│   ├── index.html
│   └── update.html
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

```bash
# Repository clone karo
git clone https://github.com/ahmadhasssan461-hub/Flask-Todo-App.git

# Folder mein jao
cd Flask-Todo-App

# Virtual environment banao
python -m venv .venv

# Activate karo (Windows)
.venv\Scripts\activate

# Required packages install karo
pip install flask flask_sqlalchemy

# App run karo
python main.py
```

Browser mein jao:
```
http://127.0.0.1:5000
```

---

## 🧠 Skills Learned
- Flask Routing (`@app.route`)
- Flask-SQLAlchemy (Database Models, ORM)
- CRUD Operations
- Jinja2 Templating (`{% for %}`, `{{ }}`)
- HTML Forms (GET/POST methods)
- Bootstrap Styling

---

## 📝 Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Display all tasks |
| `/add` | POST | Add a new task |
| `/update/<sno>` | GET | Display update form |
| `/update/<sno>` | POST | Update the task |
| `/delete/<sno>` | GET | Delete the task |

---

## 👨‍💻 Author
Made with 💻 while learning Flask
Created by M Ahmed Hasan 
