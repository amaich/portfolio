from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import re
import db
import psycopg2
from config import TOKEN, my_id

conn = psycopg2.connect("dbname=reminder_app user=postgres password=qwerty123 host=ovz3.j90259871.0n03n.vps.myjino.ru port=49321") # 9010
cursor = conn.cursor()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class remind_state(StatesGroup):
    remind = State()
    time = State()

async def start_bot(_):
    await bot.send_message(my_id, 'started')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("start")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("help")

@dp.message_handler()
async def get_remind_text(message: types.Message):
    if message.text[:11].lower() == "напомни мне":
        await remind_state.remind.set()
        state = Dispatcher.get_current().current_state()
        await state.update_data(remind=message.text[11:].strip())
        await message.answer('Во сколько?')
        await remind_state.time.set()
    else:
        await message.answer('Не понимаю, о чем ты')

@dp.message_handler(state=remind_state.time)
async def get_time_remind(message: types.Message, state: FSMContext):

    remind_time = re.search(r'([0-1][0-9]|2[0-3]):[0-6][0-9]', message.text)

    # Проверка корректности формата введенного времени
    if remind_time == None: 
        await message.answer('Введите корректное время')
        return

    await state.update_data(time=remind_time.group(0))
    data = await state.get_data()
    await message.answer(f"я напомню вам {data['remind']} в {data['time']}")
    
    db.ins(conn, cursor, message.from_user.id, data['remind'], data['time'])

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start_bot)

cursor.close()
conn.close()