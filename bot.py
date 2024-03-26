import asyncio
import logging
import sys
import threading
from datetime import datetime
from db.db_init import init_db
import loader
from aiogram import Bot, Dispatcher

from app import flask_start
from loader import bot, dp, scheduler, TEST_CHAT_ID


async def test(bot: Bot, TEST_CHAT_ID):
    await bot.send_message(TEST_CHAT_ID, f'Regular_msg, current time: {datetime.now()}')


async def main() -> None:
    init_db()

    scheduler.add_job(test, 'interval', args=(bot, TEST_CHAT_ID), seconds=3, id='edit_msg_job')
    scheduler.start()

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    flask_thread = threading.Thread(target=flask_start)
    flask_thread.start()

    asyncio.run(main())
