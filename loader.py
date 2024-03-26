import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN


bot: Bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
dp = Dispatcher()

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

scheduler = AsyncIOScheduler(timezone='Europe/Kiev')

TEST_CHAT_ID = -1001778798420
