from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud
from pydantic import BaseModel

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class CourseCreate(BaseModel):
    name: str
    description: str
    duration: int

# POST: Add a new software course
@app.post("/courses/", response_model=CourseCreate)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(**course.dict())
    return crud.create_course(db=db, course=db_course)

# GET: Retrieve a list of software courses
@app.get("/courses/")
def read_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db=db)
