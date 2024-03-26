import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///light.db', echo=True)
Session = sessionmaker(engine)

def init_db():
    Base.metadata.create_all(engine)
