from db_init import engine, Session
from sqlalchemy import select

from models import Settings


def add_user_to_db(user_id):
    with Session() as session:
        stmt = ...


def get_settings(chat_id: str | int):
    with Session() as session:
        stmt = select(Settings).where(Settings.chat_id == str(chat_id))
        result = session.execute(stmt)
    row = result.one_or_none()
    return row
