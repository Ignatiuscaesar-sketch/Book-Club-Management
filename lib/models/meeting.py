from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base
from .member import Member
from .book import Book

class Meeting(Base):
    __tablename__ = 'meetings'
    
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    date = Column(Date, nullable=False)
    notes = Column(String)
    
    member = relationship(Member)
    book = relationship(Book)
    
    def __repr__(self):
        return f"<Meeting(date='{self.date}', member='{self.member.name}', book='{self.book.title}')>"
