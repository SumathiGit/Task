from sqlalchemy.orm import Session
import datetime
import models


def create_student(db: Session,roll_no:int, name:str, dob:datetime.date):
    db_student = models.Student(roll_no= roll_no, name= name, dob= dob)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def add_mark(db: Session, student_id:int, mark:str):
    db_mark = models.Marks(student_id= student_id, mark= mark)
    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)
    return db_mark




