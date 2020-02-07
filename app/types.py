from typing import List, Optional
from pydantic import BaseModel



class Message(BaseModel):
    """ messages type """
    id: int 
    content: str 
    moment: int 
    sender_id: int 
    receiver_id: int 

    class Config:
        orm_mode = True


class User(BaseModel):
    """ users type """
    id: int = None
    name: str
    phone_number: str
    messages: List[Message] = []

    class Config:
        orm_mode = True
