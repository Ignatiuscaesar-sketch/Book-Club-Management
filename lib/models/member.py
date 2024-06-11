from . import Base
from sqlalchemy import Column, Integer, String

class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Member(name='{self.name}', email='{self.email}')>"
