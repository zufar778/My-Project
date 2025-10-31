from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command


sos_router = Router()


@sos_router.message(Command("sos"))
async def SosFile(message: Message):
    try:
        if message.from_user.id == 1740889690:
            file = FSInputFile("mahsulot.db")
            await message.answer_document(file, caption="This is the mahsulot.db file 📂")
    except Exception as e:
        await message.answer(f"Error: {e}")