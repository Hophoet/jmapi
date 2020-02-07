from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    """ users model """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, index=True)

    messages = relationship('Message', back_populates='user')



class Message(Base):
    """ messages model """
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    moment = Column(Integer, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer
        # ,ForeignKey('users.id')
        )
    user = relationship('User', back_populates='messages')
    

