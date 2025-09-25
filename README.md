# 📝Diary App

A simple Note Taking & Sharing Application built with FastAPI and PostgreSQL.
Users can register, create notes, and securely share them with other users.
Authentication is handled with JWT tokens to ensure only authorized users can access or share notes.

---

## 🚀 Features

* 🔐 **User Authentication**

  * Register & Login with hashed passwords
  * JWT-based authentication

* 📝 **Notes Management (CRUD)**

  * Create, Read, Update, Delete notes
  * Each note belongs to a user

* 🤝 **Note Sharing**

  * Share notes with other registered users
  * Shared users can view notes
  * Owner can revoke sharing

* ✅ **Access Control**

  * Only note owners & shared users can view shared notes
  * Unauthorized access is restricted

---

## 🛠️ Tech Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Tokens)
* **Password Hashing:** Passlib (bcrypt)

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
.env                 
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
   venv\Scripts\activate      
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**
   Create a database:

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

6. **Run database migrations** (if using Alembic or just create tables from models)

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

## 🧪 Testing

* Use **pytest** for unit tests
* Manual testing via **Postman** or **Insomnia**
* Run tests:

  ```bash
  pytest
  ```

---

## 📖 Future Improvements

* Add search & filtering for notes
* Allow multiple users per shared note (many-to-many)
* Add frontend (React/Next.js)
* Implement email notifications when a note is shared

---

## 👨‍💻 Author

Developed by **[Your Name]**
For the **Take-Home Assignment** on **FastAPI + PostgreSQL**

---

Would you like me to also generate a **`requirements.txt` file** for you with all the dependencies (FastAPI, SQLAlchemy, psycopg2, passlib, python-jose, python-dotenv, etc.) so you can include it in your project?
