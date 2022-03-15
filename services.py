from model import User
# from schema import CreateUser

def createUser(db, user):
    db_user = User(email = user.email, password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def checkUser(db,checkuser):
    db.query(User).filter(User.email == checkuser.email).first()
    db.query(User).filter(User.password == checkuser.password).first()
    return True