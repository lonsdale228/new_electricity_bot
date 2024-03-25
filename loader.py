import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

scheduler = AsyncIOScheduler(timezone='Europe/Minsk')