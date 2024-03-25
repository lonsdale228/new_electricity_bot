class User:
    __tablename__ = 'users'


class Timetable:
    __tablename__ = 'timetables'

    start_time = ''
    end_time = ''
    zone_type = ''


class ElectricityState:
    __tablename__ = 'electricity_states'

    start_time = ''
    end_time = ''
    total_time = ''
    zone_type = ''
