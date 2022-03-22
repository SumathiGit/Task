from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.sql.sqltypes import DATE, DateTime, String
from database import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    roll_no = Column(Integer, unique = True)
    name = Column(String)
    dob = Column(DATE)


class Marks(Base):
    __tablename__= 'marks'
    id = Column(Integer, primary_key=True)
    mark = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(String, default = True)
    student_id = Column(Integer, ForeignKey('students.id'))
    


