# Creating a telegram bot to classify the bee swarming
import aiogram
from aiogram import Bot, Dispatcher, executor, types

from predict import predict_bee_swarming

bot = Bot(token='5346782906:AAGuSoPx1rBt1xDSjI7LQVeVDvzo0ewWY84')
dp = Dispatcher(bot)

@dp.message_handler(content_types=["photo"])
async def test(message):

    await message.photo[-1].download('test.jpg')
    await message.answer(predict_bee_swarming("test.jpg"))




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




