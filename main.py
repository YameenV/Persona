from fastapi import FastAPI
from sqlalchemy.orm import Session
from model import User
from schema import CreateUser
import services as sr
from db import SessionLocal, engine
from fastapi import Depends
from db import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/createUser/", response_model=CreateUser)
def createUser(user:CreateUser, db: Session = Depends(get_db)):
    return sr.createUser(db, user)

@app.post("/checkUser/")
def checkUser(checkuser:CreateUser ,db: Session = Depends(get_db)): 
    return sr.checkUser(db, checkuser)