import logging
import asyncio
from aiogram import Dispatcher, Bot, F
from config import bot_token, admins
from user import router as register
from karzinka import z_router
from admin import a_router
from admin_add_product import adm_router
from sos import sos_router




dp = Dispatcher()
bot = Bot(token=bot_token)
logging.basicConfig(level=logging.INFO)


dp.include_router(register)
dp.include_router(z_router)
dp.include_router(a_router)
dp.include_router(adm_router)
dp.include_router(sos_router)


async def main():
    for id in admins:
        await bot.send_message(chat_id=id, text="The bot has started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"The bot is over {error}")