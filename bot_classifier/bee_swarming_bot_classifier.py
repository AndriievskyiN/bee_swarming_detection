# Creating a telegram bot to classify the bee swarming
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import os

from predict import predict_bee_swarming

bot = Bot(token='5346782906:AAGuSoPx1rBt1xDSjI7LQVeVDvzo0ewWY84')
dp = Dispatcher(bot)

# Initialize buttons to check if the photo is actually bee swarming or not
yesbtn = InlineKeyboardButton("yes", callback_data="yes")
nobtn = InlineKeyboardButton("no", callback_data="no")
yesnokboard = InlineKeyboardMarkup().add(yesbtn, nobtn)

@dp.message_handler(content_types=["photo"])
async def test(message):

    await message.photo[-1].download('test.jpg')
    await message.answer(predict_bee_swarming("test.jpg"), reply_markup=yesnokboard)


# Manage yes vs no button actions
@dp.callback_query_handler(text=["yes","no"])
async def manage_model_checks(call: types.CallbackQuery):
    if call.data == "yes":
        os.system("mv test.jpg ../images/bee_swarming")
    else:
        os.system("mv test.jpg  ../images/clear_sky") 


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




