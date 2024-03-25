from db.db_init import Base

class User(Base):
    __tablename__ = 'users'


class Timetable(Base):
    __tablename__ = 'timetables'

    start_time = ''
    end_time = ''
    zone_type = ''


class ElectricityState(Base):
    __tablename__ = 'electricity_states'

    start_time = ''
    end_time = ''
    total_time = ''
    zone_type = ''
