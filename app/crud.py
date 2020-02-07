from sqlalchemy.orm import Session

from . import models, types

#MESSAGES 
def get_messages(database: Session, skip: int = 0, limit: int = 100):
    """ messages getter """
    messages = database.query(models.Message).offset(skip).limit(limit).all()
    return messages

#USERS
def get_users(database: Session, skip: int = 0, limit: int = 100):
    """ users getter """
    users = database.query(models.User).offset(skip).limit(limit).all()
    return users

def create_user(db: Session, user: types.User):
    db_user = models.User(name=user.name, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_phone_number(database: Session, phone_number: str):
    """ user getter by phone_number """
    user =  database.query(models.User).filter(models.User.phone_number == phone_number).first()
    return user
