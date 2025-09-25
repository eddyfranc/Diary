from fastapi import FastAPI
from app.database import Base, engine
from app.models import user
from app.routes import auth

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(title="Diary Note App")

# Register routers
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Diary Note App 🚀"}
