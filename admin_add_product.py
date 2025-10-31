from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from db import MaxsulotlarAdds
from states import Admin_add
from aiogram.fsm.context import FSMContext
from config import admins


adm_router = Router()


@adm_router.message(Command('add'))
async def added(message: Message, state: FSMContext):
    user_id = message.from_user.id
    for i in admins:
        if user_id == i:
            await message.answer("Enter a product name: ")
            await state.set_state(Admin_add.name1)


@adm_router.message(F.text, Admin_add.name1)
async def named(message: Message, state: FSMContext):
    xabar = message.text
    await state.update_data(name=xabar)
    await message.answer("Enter a product price: ")
    await state.set_state(Admin_add.price1)


@adm_router.message(F.text, Admin_add.price1)
async def named(message: Message, state: FSMContext):
    xabar = message.text
    await state.update_data(price=xabar)
    await message.answer("Enter a product picture: ")
    await state.set_state(Admin_add.picture)


@adm_router.message(F.photo, Admin_add.picture)
async def named(message: Message, state: FSMContext):
    xabar = message.photo[-1].file_id
    await state.update_data(image=xabar)
    await message.answer("About product: ")
    await state.set_state(Admin_add.about)


@adm_router.message(F.text, Admin_add.about)
async def named(message: Message, state: FSMContext):
    xabar = message.text
    print(xabar)
    data = await state.get_data()
    name = data.get('name')
    price = data.get('price')
    image = data.get('image')
    description = xabar
    print('zgf')
    MaxsulotlarAdds(name, price, image, description)
    await message.answer("added")
    await state.clear()
        


