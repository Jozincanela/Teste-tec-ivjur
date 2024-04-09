from database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class Users (Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    
class Users_Request (BaseModel):
    username: str
    email: str

    class Config:
        json_schema_extra = {   
            'example': {
                "username": "user name example",
                "email": "useremailexample@user.com"
            }
        }