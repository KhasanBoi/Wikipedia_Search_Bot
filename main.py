import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5076506556:AAEEb92ZOk7iY0XXjSLeSoVFcLyYykTwSnk'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)  # check bot for new messages and requests and connects with backend

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def wikiData(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi :(')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)