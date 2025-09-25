# 📝 Diary App

A simple **Note Taking & Sharing Application** built with **FastAPI** and **PostgreSQL**.
Users can register, create personal notes, and securely share them with other users.
Authentication is powered by **JWT tokens**, ensuring only authorized users can access or share notes.
Database migrations are managed with **Alembic** for scalability and maintainability.

---

## 🚀 Features

* 🔐 **User Authentication**

  * Register & login with hashed passwords
  * JWT-based authentication (access tokens)

* 📝 **Notes Management (CRUD)**

  * Create, read, update, delete notes
  * Each note belongs to a user

* 🤝 **Note Sharing**

  * Share notes with other registered users
  * Shared users can view notes
  * Owners can revoke access

* ✅ **Access Control**

  * Only note owners & explicitly shared users can view a note
  * Unauthorized access is blocked

* ⚡ **Migrations with Alembic**

  * Version-controlled schema changes
  * Easy upgrades/downgrades of database schema

---

## 🛠️ Tech Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Migrations:** Alembic
* **Authentication:** JWT (JSON Web Tokens)
* **Password Hashing:** Passlib (bcrypt)
* **Environment Config:** python-dotenv

---

## 📂 Project Structure

```
app/
 ┣ models/            
 ┃ ┣ user.py
 ┃ ┣ note.py
 ┃ ┗ shared_note.py
 ┣ schemas/             
 ┃ ┣ user.py
 ┃ ┣ note.py
 ┃ ┣ shared_note.py
 ┃ ┗ token.py
 ┣ routes/             
 ┃ ┣ auth.py
 ┃ ┣ note_routes.py
 ┃ ┗ shared_notes.py
 ┣ database.py         
 ┣ main.py             
alembic/                
 ┣ versions/            
.env                    
requirements.txt        
README.md               
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/fastapi-diary-app.git
   cd fastapi-diary-app
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**

   ```sql
   CREATE DATABASE diary;
   ```

5. **Configure `.env` file**

   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/diary
   SECRET_KEY=your-secret-key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

6. **Run database migrations with Alembic**

   ```bash
   alembic upgrade head
   ```

7. **Start the development server**

   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📌 API Endpoints

### 🔑 Authentication

* `POST /auth/register` → Register a new user
* `POST /auth/login` → Login & get JWT token

### 📝 Notes

* `POST /notes/` → Create a new note
* `GET /notes/` → List my notes
* `GET /notes/{id}` → Get a note by ID
* `PUT /notes/{id}` → Update a note
* `DELETE /notes/{id}` → Delete a note

### 🤝 Shared Notes

* `POST /notes/{id}/share` → Share a note with another user
* `GET /shared-notes/` → List notes shared with me

---
