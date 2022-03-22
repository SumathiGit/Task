from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import student



models.Base.metadata.create_all(bind=engine) 

app = FastAPI(title="Student_Management_System")

app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student.router)



@app.get("/")
async def root():
    return {"message": "My StudentDB Management System!"}