from lib.models import Base, engine
from lib.models.member import Member
from lib.models.book import Book
from lib.models.meeting import Meeting

# Create all tables in the database
Base.metadata.create_all(engine)
print("Tables created successfully!")
