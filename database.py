from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database file
sqlalchemy_database_url = "sqlite:///./tasks.database.db"

# Database connection (engine)
engine = create_engine(sqlalchemy_database_url, connect_args={"check_same_thread": False})

# Sessions 4 Database
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class
base = declarative_base()
