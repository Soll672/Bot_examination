from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database.db import save_homework_to_db


homework_router = Router()


class HomeworkForm(StatesGroup):
    name = State()
    group = State()
    homework_number = State()
    github_link = State()


@homework_router.message(commands=["homework"])
async def start_homework_dialog(message: types.Message, state: FSMContext):
    await state.set_state(HomeworkForm.name)
    await message.answer("Пожалуйста, введите ваше имя:")

@homework_router.message(HomeworkForm.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(HomeworkForm.group)
    group_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add("Python 01-1", "Python 02-1", "WebDev 03-1")
    await message.answer("Выберите вашу группу:", reply_markup=group_keyboard)

@homework_router.message(HomeworkForm.group)
async def process_group(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    await state.set_state(HomeworkForm.homework_number)
    homework_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*(str(i) for i in range(1, 9)))
    await message.answer("Введите номер домашнего задания (от 1 до 8):", reply_markup=homework_keyboard)

@homework_router.message(HomeworkForm.homework_number)
async def process_homework_number(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or not (1 <= int(message.text) <= 8):
        await message.answer("Номер ДЗ должен быть от 1 до 8. Попробуйте снова.")
        return
    await state.update_data(homework_number=int(message.text))
    await state.set_state(HomeworkForm.github_link)
    await message.answer("Введите ссылку на GitHub (https://github.com):", reply_markup=types.ReplyKeyboardRemove())

@homework_router.message(HomeworkForm.github_link)
async def process_github_link(message: types.Message, state: FSMContext):
    if not message.text.startswith("https://github.com"):
        await message.answer("Ссылка должна начинаться с 'https://github.com'. Попробуйте снова.")
        return
    await state.update_data(github_link=message.text)
    user_data = await state.get_data()
    save_homework_to_db(
        user_data['name'],
        user_data['group'],
        user_data['homework_number'],
        user_data['github_link']
    )
    await message.answer("Домашнее задание успешно сохранено!")
    await state.clear()
