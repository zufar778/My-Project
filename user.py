from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from inline_buttons import menu, MenuButtons, RaqamButtons
from db import Mahsulotlar, MaxsulotlarAdds, add
from states import Product
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(CommandStart())
async def StartBot(message: Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        name = message.from_user.first_name
        username = message.from_user.username
        add(user_id, name, username)
        await message.answer_photo(photo="https://www.arzaan.pk/cdn/shop/articles/3.jpg", caption=f"Assalomu aleykum Do'konimizga Xush kelibsiz\n\n{message.from_user.first_name}", reply_markup=menu)

    except:
        await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Shopping_online_with_bank_card.jpg/1200px-Shopping_online_with_bank_card.jpg", caption=f"Welcome back to our market\n\n{message.from_user.first_name}", reply_markup=menu)


@router.message(Command("help"))
async def HelpBot(message: Message):
    await message.answer(text="Botdan foydalanish uchun /start buyrug'ini yuboring!")
    

@router.callback_query(F.data=="Menu")
async def MenuBot(call: CallbackQuery, state: FSMContext):
    await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSykUhFDLt30fbBfTxIm4h-tCKn8u9T-MKgQ&s", caption="Our products !!", reply_markup=MenuButtons())
    await state.set_state(Product.go)
    # await call.message.answer_photo(photo="https://g2u-wp-prod.s3-ap-southeast-2.amazonaws.com/wp-content/uploads/2022/09/Online-shopping-hero.jpg", caption="Our products !!", reply_markup=MenuButtons())


@router.callback_query(Product.go)
async def MahsulotBots(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    print(xabar)

    if xabar == 'Back':
        await call.message.answer('Choose:', reply_markup=menu)

    for text in Mahsulotlar():
        if text[1] == xabar:
            await call.message.answer_photo(
                photo=text[3],
                caption=f"Name: {text[1]}\nPrice: {text[2]}\nAbout: {text[4]}",
                reply_markup=RaqamButtons()
            )
            await state.update_data(name=text[1], price=text[2])
            await state.set_state(Product.yes)
            break
    else:
        await call.answer("There is no such kind of product")

   



# @router.callback_query(F.data, Product.go)
# async def MahsulotBots(call: CallbackQuery, state: FSMContext):
#     xabar = call.data
#     print(xabar)
#     for text in Mahsulotlar():
#         if text[1] == xabar:
#             await call.message.answer_photo(photo=f"{text[3]}", caption=f"Name: {text[1]}\nPrice: {text[2]}\nAbout: {text[4]}", reply_markup=RaqamButtons())
#             await state.update_data(name=f"{text[1]}", price=f"{text[2]}")
#             await state.set_state(Product.go)
#             break
#         elif xabar=='Back':
#             await state.set_state(Product.go)
#             await call.message.answer('Choose:', reply_markup=menu)
#             break
#     else:
#         await call.answer("There is no such kind of product")


@router.callback_query(Product.yes)
async def Number(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    if xabar.isdigit():
        print(xabar)
        data = await state.get_data()
        name = data.get('name')
        price = float(data.get('price'))
        xabar = int(call.data)
        user_id = call.from_user.id
        print(xabar*price)
        MaxsulotlarAdds(user_id=user_id, name=name, price=(xabar*price), count=xabar)
        await call.message.answer('Added')
        await state.set_state(Product.go)
        await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcHonklFE4W7nig3kENhDdsNJHqbPGOELnnA&s.jpg", caption="Our products !!", reply_markup=MenuButtons())
    else:
        await state.set_state(Product.go)
        await call.message.answer_photo(photo=f"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSBmFzBZmw2PIm94-J3P8PV-U0rzBCk2AnHuNShOkATN9ELYoK0w9iNnqBurCxIl4fRJA&usqp=CAU.jpg", caption="Our products !!", reply_markup=MenuButtons())
        await state.clear()
    # try:
    #     data = await state.get_data()
    #     name = data.get('Name')
    #     price = float(data.get('Price'))
    #     xabar = int(call.data)
    #     user_id = call.from_user.id
    #     print(xabar*price)
    #     MaxsulotlarAdds(user_id=user_id, name=name, price=(xabar*price), count=xabar)
    #     await call.message.answer('Added')
    #     await state.clear()
    #     await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcHonklFE4W7nig3kENhDdsNJHqbPGOELnnA&s.jpg", caption="Our products !!", reply_markup=MenuButtons())
    
    # except:
    #     await state.set_state(Product.go)
    #     await call.message.answer_photo(photo=f"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSBmFzBZmw2PIm94-J3P8PV-U0rzBCk2AnHuNShOkATN9ELYoK0w9iNnqBurCxIl4fRJA&usqp=CAU.jpg", caption="Our products !!", reply_markup=MenuButtons())

    