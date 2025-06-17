# Flask Multi-Backend Database Support

[![CodeQL Advanced](https://github.com/cagatay-softgineer/flask-backend/actions/workflows/codeql.yml/badge.svg)](https://github.com/cagatay-softgineer/flask-backend/actions/workflows/codeql.yml)

This project provides a clean and modular backend setup for Flask applications with support for multiple database backends: PostgreSQL, SQLite, MySQL, MongoDB, and Firebase/Firestore. It uses `psycopg2`, `pymysql`, `pymongo`, and `google-cloud-firestore` for database interactions, `pydantic` for environment configuration, and Flask **Blueprints** to organize routes and avoid spaghetti code.

## 📦 Project Structure

```
/project-root
├── server.py (or main.py)       # Your Flask application entrypoint
├── config/
│   └── settings.py              # Pydantic-based environment config
├── database/                    # Connection managers for each backend
│   ├── __init__.py              # Dynamic get_connection loader
│   ├── postgres.py
│   ├── sqlite.py
│   ├── mysql.py
│   ├── mongodb.py
│   └── firebase.py
├── Blueprints/                  # Modular route definitions
│   ├── auth.py                  # Authentication routes
│   └── __init__.py              # Blueprint registry
├── util/
│   └── blueprints.py            # Function to register all blueprints
├── requirements.txt             # Python dependencies
├── .env                         # Environment configuration
└── README.md                    # This file
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd project-root
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
3. Create a `.env` file at the project root (see **Environment Variables** below).

## 🌐 Environment Variables

Use `.env` to configure your app. At minimum, you must set:

```dotenv
# Generic
DB_TYPE=postgres         # One of: postgres, sqlite, mysql, mongodb, firebase
DATABASE_URL=            # Optional URL fallback for SQL or MongoDB

# PostgreSQL (if used)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=yourdb

# SQLite (if used)
SQLITE_PATH=./data.sqlite

# MySQL (if used)
MYSQL_URI=mysql://user:pw@host:3306/dbname

# MongoDB (if used)
MONGODB_URI=mongodb+srv://user:pw@cluster0.mongodb.net/dbname

# Firebase/Firestore (if used)
FIREBASE_PROJECT_ID=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

# App secrets
JWT_SECRET_KEY=supersecretjwtkey
SALT=somesecretsalt
```

Only fill the variables relevant to your `DB_TYPE`.

## 🚀 Usage

### Registering Blueprints

In your Flask app entrypoint (e.g. `util/blueprints.py`), import and register your Blueprints for clean route organization:

```python
from flask import Flask
from util.blueprints import register_blueprints
from database import get_connection

app = Flask(__name__)

# Register all Blueprints (auth, user, token, etc.)
register_blueprints(app)

@app.route('/status')
def status():
    return {'status': 'ok'}

# Example endpoint using dynamic DB
@app.route('/users')
def list_users():
    with get_connection() as db:
        # PostgreSQL/MySQL/SQLite: use db.cursor()/commit()
        # MongoDB: use db['users'].find()
        # Firestore: use db.collection('users').stream()
        ...
```

This keeps route logic modular and avoids clutter in a single file.

## 🔐 Features

- **Dynamic database selection** via `DB_TYPE`
- **Modular routing** with Flask Blueprints
- **Secure configuration** with `pydantic`
- **Support for relational (Postgres, MySQL, SQLite) and NoSQL (MongoDB, Firestore)**
- **Context-managed connections** to ensure cleanup
- **Extensible**: add new backends by creating a module in `database/`; add new feature routes by creating Blueprints.

## 📝 Contributing

Contributions are welcome! Please open issues or pull requests.

## 📄 License

[License](LICENSE)
