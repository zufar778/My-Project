from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from reply import contact_phone
from inline_buttons import menu
from config import admins


a_router = Router()


@a_router.callback_query(F.data=='Contact us')
async def sending(call: CallbackQuery,  state: FSMContext):
    for i in admins:
        xabar = f"[{call.from_user.full_name}](tg://user_id={call.from_user.id})"
        await call.message.answer("Request sent")
        
        await call.bot.send_message(chat_id=i, text=f"You have a message from {xabar}", parse_mode="MarkdownV2", reply_markup=menu)
