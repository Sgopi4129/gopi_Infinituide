from sqlalchemy.orm import Session
from . import models

def get_courses(db: Session):
    return db.query(models.Course).all()

def create_course(db: Session, course: models.Course):
    db.add(course)
    db.commit()
    db.refresh(course)
    return course
