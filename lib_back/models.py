from sqlalchemy import Column, Integer, String, Date
from database import Base

class Library(Base):
    __tablename__="books"

    isbn = Column(Integer, primary_key=True)
    book_title = Column(String(255), nullable=False)
    book_author = Column(String(255), nullable=False)
    year_of_publication = Column(Date, nullable=False)
    publisher = Column(String(255), nullable=False)