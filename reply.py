from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


contact_phone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share contact", request_contact=True)]
    ],
    resize_keyboard=True
)

location_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share location", request_location=True)]
    ],
    resize_keyboard=True
)