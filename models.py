from sqlalchemy import Integer, Column, String, Boolean, DateTime

from db.db_init import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True)
    tg_id = Column(String, unique=True, primary_key=True)
    is_admin = Column(Boolean, default=False)

class Timetable(Base):
    __tablename__ = 'timetables'

    id = Column(Integer, autoincrement=True, primary_key=True)

    start_time = Column(DateTime)
    end_time = Column(DateTime)
    zone_type = Column(Integer)
    group_num = 0


class ElectricityState(Base):
    __tablename__ = 'electricity_states'

    start_time = Column(DateTime)
    end_time = Column(DateTime)
    total_time = Column(DateTime)
    zone_type = Column(Integer)


class Settings(Base):
    __tablename__ = 'settings'

    receive_requests = Column(Boolean)
    current_group = Column(Integer)
    chat_id = Column(String, unique=True)
    edit_time = Column(Integer)
