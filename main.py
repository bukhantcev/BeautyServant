import logging
import os

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('TOKEN')
#chat_id_admin = -1001911875283


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot)



@dp.message_handler(content_types="new_chat_members")
async def on_user_join(message: types.Message):
    print(message.chat.id)
    await message.delete()
    await bot.send_message(text='Bot rabotaet!))', chat_id= 404354012)

@dp.message_handler(content_types="left_chat_member")
async def on_user_join(message: types.Message):
    print(message.chat.id)
    await message.delete()
    await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')

@dp.message_handler(content_types="new_chat_title")
async def on_user_join(message: types.Message):
    print(message.chat.id)
    await message.delete()
    await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')

@dp.message_handler(content_types="new_chat_photo")
async def on_user_join(message: types.Message):
    print(message.chat.id)
    await message.delete()
    await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')

@dp.message_handler(content_types="delete_chat_photo")
async def on_user_join(message: types.Message):
    print(message.chat.id)
    await message.delete()
    await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
