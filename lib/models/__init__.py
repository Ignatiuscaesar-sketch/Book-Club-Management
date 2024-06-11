from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///bookclub.db')
Session = sessionmaker(bind=engine)
session = Session()

# Importing the models to create the tables
from .member import Member
from .book import Book
from .meeting import Meeting
from .user import User

Base.metadata.create_all(engine)
