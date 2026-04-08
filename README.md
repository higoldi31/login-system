# Django Login System

A simple Django web application that allows users to register, log in, and access a protected homepage.

Live link : https://login-system-w8h7.onrender.com
---

## Features

- User registration (Sign Up)
- User authentication (Login / Logout)
- Protected homepage accessible only to logged-in users
- Redirects unauthenticated users to the login page

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (Django templates)
- **Database:** SQLite (default)

---

## Project Structure

```
your_project/
├── manage.py
├── db.sqlite3
├── registration/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── app1/              # App handling auth
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
        ├── signup.html
        ├── login.html
        └── home.html
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Open your browser and visit:**

   ```
   http://127.0.0.1:8000/
   ```

---

## Usage

| Page       | URL          | Description                              |
|------------|--------------|------------------------------------------|
| Sign Up    | `/signup/`   | Register a new user account              |
| Login      | `/login/`    | Log in with existing credentials         |
| Homepage   | `/home/`     | Protected page, visible after login only |
| Logout     | `/logout/`   | Logs out and redirects to login page     |

---

## Configuration

Settings are located in `your_project/settings.py`. Key settings:

- `SECRET_KEY` — Change this to a strong secret key in production.
- `DEBUG` — Set to `False` in production.
- `DATABASES` — Defaults to SQLite. Replace with PostgreSQL or MySQL for production.
- `LOGIN_REDIRECT_URL` — Where users are sent after a successful login (default: `/home/`).
- `LOGIN_URL` — Where unauthenticated users are redirected (default: `/login/`).

---

## Running Tests

```bash
python manage.py test
```

---

## Future Improvements

- Password reset via email
- Remember me / persistent sessions
- OAuth login (Google, GitHub)
- User profile page
- Django REST Framework API support

---

