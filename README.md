# Netlon Backend

Netlon Backend is a RESTful API built using Flask (Python).  
This project handles backend operations including authentication, user management, quotations, inventory management, and dashboard functionalities.

It is designed to work with a React frontend and provides secure, scalable, and modular API endpoints.

---

## 🚀 Features

- User Authentication (JWT-based)
- User Management (CRUD)
- Quotation Management
- Inventory Management
- Dashboard APIs
- Database Integration using SQLAlchemy
- Database Migrations using Flask-Migrate
- CORS Enabled for Frontend Integration
- Modular Project Structure

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- MySQL
- REST API Architecture

---

## 📁 Project Structure

```
netlonbackend/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── __init__.py
│
├── migrations/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```
git clone https://github.com/Thiksha-6/netlonbackend.git
cd netlonbackend
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate virtual environment:

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Create a MySQL database and update `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/netlon_db"
```

---

## 🔄 Run Migrations

```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## ▶️ Run the Application

```
python run.py
```

Server will run at:
```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### Authentication
- POST /api/login

### Users
- GET /api/users
- POST /api/users
- PUT /api/users/<id>
- DELETE /api/users/<id>

### Quotations
- GET /api/quotations
- POST /api/quotations
- DELETE /api/quotations/<id>

### Inventory
- GET /api/inventory
- POST /api/inventory
- PUT /api/inventory/<id>
- DELETE /api/inventory/<id>

---

## 🔐 Environment Variables (Optional)

```
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
```

---

## 👩‍💻 Author

Mahalakshmi M  
Full Stack Developer
