import logging

import asyncio
import os
import random
import time

from fsm_config import NewItem
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

memory = MemoryStorage()

#API_TOKEN = os.getenv('TOKEN')
API_TOKEN = '6283280993:AAHi8EqmQ41zE8rLl_0ayUexaX69DlCxs20'
chat_id_admin = -1001911875283


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=memory)

# @dp.message_handler(content_types='sticker')
# async def allll(message: types.Message):
#     print(message)



@dp.message_handler(content_types="new_chat_members")
async def on_user_join(message: types.Message):
    if message.chat.id == chat_id_admin:
        print(message.chat.id)
        await message.delete()
        await bot.send_message(text='Bot rabotaet!))', chat_id= 404354012)

@dp.message_handler(content_types="left_chat_member")
async def on_user_join(message: types.Message):
    if message.chat.id == chat_id_admin:
        print(message.chat.id)
        await message.delete()
        await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')

@dp.message_handler(content_types="new_chat_title")
async def on_user_join(message: types.Message):
    if message.chat.id == chat_id_admin:
        print(message.chat.id)
        await message.delete()
        await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')

@dp.message_handler(content_types="new_chat_photo")
async def on_user_join(message: types.Message):
    if message.chat.id == chat_id_admin:
        print(message.chat.id)
        await message.delete()
        await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')

@dp.message_handler(content_types="delete_chat_photo")
async def on_user_join(message: types.Message):
    if message.chat.id == chat_id_admin:
        print(message.chat.id)
        await message.delete()
        await bot.send_message(chat_id=404354012, text='Bot rabotaet!))')




@dp.message_handler(commands=['pusk'],state=None)
async def go_random(message:types.Message, state:FSMContext):
    #if message.chat.id == chat_id_admin:
    await message.answer('Send list')
    await NewItem.random.set()


@dp.message_handler(state=NewItem.random)
async def result(message:types.Message, state:FSMContext):
    my_list = message.text.split('\n')
    await message.answer('Ready')
    await asyncio.sleep(2)
    await bot.edit_message_text(text='5', chat_id=message.chat.id, message_id=message.message_id+1)
    await asyncio.sleep(1)
    await bot.edit_message_text(text='4', chat_id=message.chat.id, message_id=message.message_id + 1)
    await asyncio.sleep(1)
    await bot.edit_message_text(text='3', chat_id=message.chat.id, message_id=message.message_id + 1)
    await asyncio.sleep(1)
    await bot.edit_message_text(text='2', chat_id=message.chat.id, message_id=message.message_id + 1)
    await asyncio.sleep(1)
    await bot.edit_message_text(text='1', chat_id=message.chat.id, message_id=message.message_id + 1)
    await asyncio.sleep(1)
    await bot.edit_message_text(text='0', chat_id=message.chat.id, message_id=message.message_id + 1)
    await asyncio.sleep(1)
    await bot.edit_message_text(text='Go!', chat_id=message.chat.id, message_id=message.message_id + 1)

    print(my_list)
    stop = 0
    for i in range(10):
        index = random.randint(0, len(my_list)-1)
        try:
            await bot.edit_message_text(text=my_list[index], chat_id=message.chat.id, message_id=message.message_id + 1)
            await asyncio.sleep(2)
        except:
            pass
    await message.answer_sticker(sticker="CAACAgIAAxkBAAIQtmVvHkO3UQwuZCvM7vDlBAlY2eG9AAI-HQACA7WASjKx0mTDn6TGMwQ")
    await state.finish()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




