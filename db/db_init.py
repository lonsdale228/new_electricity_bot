import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///light.db', echo=True)


async def init_db():
    Base.metadata.create_all(engine)
