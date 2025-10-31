from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db import Mahsulotlar



purchase = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Yes", callback_data="Yes"), InlineKeyboardButton(text="No", callback_data="No")]
    ]
)


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Menu 📝", callback_data="Menu")],
        [InlineKeyboardButton(text="Karzinka 🛒", callback_data="Karzinka"), InlineKeyboardButton(text="Contact us 📞", callback_data="Contact us")]
    ]
)



def MenuButtons():
    buttons = InlineKeyboardBuilder()
    for text in Mahsulotlar():
        buttons.add(InlineKeyboardButton(text=f"{text[1]}", callback_data=f"{text[1]}"))
    buttons.add(InlineKeyboardButton(text="Back 🔙", callback_data="Back"))
    buttons.adjust(2)
    return buttons.as_markup()


def RaqamButtons():
    buttons = InlineKeyboardBuilder()
    for text in range(1, 10):
        buttons.add(InlineKeyboardButton(text=f"{text}", callback_data=f"{text}"))
    buttons.add(InlineKeyboardButton(text="Back 🔙", callback_data="Back"))
    buttons.adjust(3)
    return buttons.as_markup()


order = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Order", callback_data="Order")],
        [InlineKeyboardButton(text="Clear", callback_data="Clear"), InlineKeyboardButton(text="Back", callback_data="Back")]
    ]
)