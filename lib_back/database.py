from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:0000@localhost::3306/Library?charset=utf8mb4"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()