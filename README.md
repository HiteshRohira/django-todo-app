# Todo App 📝

A simple Todo application built using **Django** to manage tasks. This project demonstrates basic CRUD (Create, Read, Update, Delete) functionality, showcasing Django's core concepts like models, views, templates, and forms.

---

## Features ✨

- View a list of tasks.
- Add new tasks with a simple form.
- Toggle task completion status.
- Delete tasks from the list.
- Responsive design using Django templates.

---

## Tech Stack ⚙️

- **Backend**: [Django](https://www.djangoproject.com/) (Python)
- **Database**: SQLite (default Django database)
- **Frontend**: HTML/CSS with Django Templates

---

## Installation 🔧

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m virtualenv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## How to Use 🛠️

1. **View Tasks**:
   - The homepage displays all tasks in the database.

2. **Add a Task**:
   - Use the form on `http://127.0.0.1:8000/add` to add a new task.

3. **Update Task Status**:
   - Click "Toggle Complete" to mark a task as completed or not completed.

4. **Delete a Task**:
   - Click "Delete" to remove a task from the database.
