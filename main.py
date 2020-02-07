from typing import List
from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from app.database import get_database
from app import crud
from app import types

#API main object
app = FastAPI()


#root endpoint
@app.get('/')
def root():
    
    return {
        'message':'Welcome on JM mobile application API'
    }

#get messages endpoint
@app.get('/messages/', response_model=List[types.Message])
def read_messages(skip: int = 0, limit: int = 100, database: Session =  Depends(get_database)):
    messages = crud.get_messages(database=database, skip=skip, limit=limit)
    return messages

#get users endpoint
@app.get('/users/', response_model=List[types.User])
def read_users(skip: int = 0, limit: int = 100, database: Session =  Depends(get_database)):
    users = crud.get_users(database=database, skip=skip, limit=limit)
    return users


@app.post('/register/')
def register(user: types.User = Body(..., embed=True),  database: Session =  Depends(get_database)):
    exist_user = crud.get_user_by_phone_number(database, user.phone_number)
    if exist_user: 
        return { 
            'text':'user already exists!',
            'user':exist_user
             }
    db_user = crud.create_user(database, user)
    exist_user = crud.get_user_by_phone_number(database, user.phone_number)
    return {
        'text': 'user created successfully!',
        'user': exist_user
        }

@app.post('/login/')
def login(phone_number: str = Body(..., embed=True),  database: Session =  Depends(get_database)):
    exist_user = crud.get_user_by_phone_number(database, phone_number)
    if exist_user: 
        return { 
            'text':'login successfully!',
            'user':exist_user
             }

    return {
        'text': 'invalid credental!'
        }