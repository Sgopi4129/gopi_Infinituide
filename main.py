from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Course model
class Course(BaseModel):
    name: str
    description: str
    level: str

# In-memory course storage (for simplicity)
courses = []

# POST endpoint to add a new course
@app.post("/courses/")
def add_course(course: Course):
    courses.append(course)
    return {"message": "Course added successfully", "course": course}

# GET endpoint to retrieve all courses
@app.get("/courses/", response_model=List[Course])
def get_courses():
    return courses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
