import asyncio
import logging
import sys
import loader
from aiogram import Bot, Dispatcher

from loader import bot, dp, scheduler, TEST_CHAT_ID


async def test(bot: Bot, TEST_CHAT_ID):
    await bot.send_message(TEST_CHAT_ID, 'Regular_msg')


async def main() -> None:
    scheduler.add_job(test, 'interval', args=(bot, TEST_CHAT_ID), seconds=3, id='edit_msg_job')
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
