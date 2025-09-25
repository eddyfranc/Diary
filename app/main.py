from fastapi import FastAPI
from app.database import Base, engine
from app.models import user, note
from app.routes import auth, note_routes, shared_notes

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(title="Diary Note App")


# Register routers
app.include_router(auth.router)
app.include_router(note_routes.router)
app.include_router(shared_notes.router)


@app.get("/")
def root():
    return {"message": "Diary"}
