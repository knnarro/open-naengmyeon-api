from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from starlette.config import Config

config = Config('.env')

SQLALCHEMY_DATABASE_URL = config('DATABASE_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()