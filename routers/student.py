from fastapi import APIRouter,Depends
import models , crud
import datetime
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal



router = APIRouter(prefix='/api/student',tags=['Student'])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add")
async def create_student(
    roll_no :int, name:str, dob:datetime.date, db: Session = Depends(get_db)):
    return crud.create_student(db=db, roll_no=roll_no,name=name, dob=dob)

@router.get("/allstudents")
async def list(db:Session = Depends(get_db)):
    _list = db.query(models.Student).all()
    return _list

@router.get("/<pk>")
async def getstudentbyid(roll_no:int, db:Session = Depends(get_db)):
    _list = db.query(models.Student).filter(models.Student.roll_no == roll_no).all()
    return _list


@router.post("/<pk>/addmark")
async def add_mark(
    student_id:int, mark:str, db: Session = Depends(get_db)):
    return crud.add_mark(db=db, student_id=student_id, mark=mark)


@router.get("/<pk>/mark")
async def getmarkbyid(student_id:int, db:Session = Depends(get_db)):
    _list = db.query(models.Marks).filter(models.Marks.student_id == student_id).all()
    return _list



@router.post("/addgrade")
async def add_grade(student_id:int, db:Session= Depends(get_db)):
    db_marks = db.query(models.Marks).filter(models.Marks.student_id == student_id).first()
    if db_marks.mark > 90:
        grade = "S"
    elif db_marks.mark >= 80 and db_marks.mark < 90:
        grade = "A"
    elif db_marks.mark >= 70 and db_marks.mark < 80:
        grade = "B"
    elif db_marks.mark >= 60 and db_marks.mark < 70:
        grade = "C"
    elif db_marks.mark >= 51 and db_marks.mark < 60:
        grade = "D"
    elif db_marks.mark >= 50 and db_marks.mark < 55:
        grade = "E"
    else:
        grade = "F"

    db_mark = models.Grade(student_id= student_id, grade=grade)
    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)
    return db_mark


@router.get("/results")
async def getstudentbygrade(grade:str, db:Session = Depends(get_db)):
    _list = db.query(models.Grade).filter(models.Grade.grade == grade).all()
    return _list



@router.get("/passpercentage")
async def passpercentage(db:Session = Depends(get_db)):
    db_students = db.query(models.Student).all()
    stu_count = 0
    f_count = 0
    for i in db_students:
        stu_count = stu_count +1 
    print(stu_count)

    db_grade = db.query(models.Grade).filter(models.Grade.grade == "F").all()
    for i in db_grade:
        f_count = f_count + 1
    print(f_count)


    pp = stu_count - f_count / stu_count * 100
    return { 'PassPercentage' : pp }




