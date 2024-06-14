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
        member_name = self.member.name if self.member else "Unknown"
        book_title = self.book.title if self.book else "Unknown"
        return f"<Meeting(date='{self.date}', member='{member_name}', book='{book_title}')>"
