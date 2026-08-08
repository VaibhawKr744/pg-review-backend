import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load variables from .env into the environment
load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

# engine: knows HOW to connect to Postgres (the URL, driver, etc.)
engine = create_engine(DATABASE_URL)

# SessionLocal: a factory — call it to get a new DB session per request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: parent class our models will inherit from
Base = declarative_base()
