# Creating a telegram bot to classify the bee swarming
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import os
from datetime import datetime

from predict import predict_bee_swarming

bot = Bot(token='5346782906:AAGuSoPx1rBt1xDSjI7LQVeVDvzo0ewWY84')
dp = Dispatcher(bot)


# Initialize buttons to check if the photo is actually bee swarming or not
yesbtn = InlineKeyboardButton("yes", callback_data="yes")
nobtn = InlineKeyboardButton("no", callback_data="no")
yesnokboard = InlineKeyboardMarkup().add(yesbtn, nobtn)

@dp.message_handler(content_types=["photo"])
async def test(message):
    global now
    now = datetime.now().strftime("%H:%M:%S")
    await message.photo[-1].download(f'test{now}.jpg')
    await message.answer(predict_bee_swarming(f"test{now}.jpg"), reply_markup=yesnokboard)


# Manage yes vs no button actions
@dp.callback_query_handler(text=["yes","no"])
async def manage_model_checks(call: types.CallbackQuery):
    if call.data == "yes":
        os.system(f"mv test{now}.jpg checked_images/bee_swarming")
        await call.message.delete()
    else:
        os.system(f"mv test{now}.jpg checked_images/clear_sky") 
        await call.message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




