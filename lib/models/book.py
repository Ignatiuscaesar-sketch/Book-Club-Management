from . import Base
from sqlalchemy import Column, Integer, String

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    status = Column(String, default='not read')  # or 'reading', 'read'
    
    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', status='{self.status}')>"
