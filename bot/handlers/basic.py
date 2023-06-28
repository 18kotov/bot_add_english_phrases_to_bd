import os
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from bot.handlers.states import AddPhrase
from aiogram.fsm.context import FSMContext
from database_functions.sql_insert import add_phrases
from bot.utils.check_phrases import check_english_phrase, check_russian_phrase
from database_functions.sql_edit import delete_phrase
from database_functions.sql_select import get_quantity_phrases_add_today

user1 = int(os.getenv('user1'))
users = {user1}


router = Router()


@router.message(CommandStart(), F.from_user.id.in_(users))
async def get_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть. Добавь новую пару фраз')
    chat_id = message.chat.id
    await message.reply(f"Hello! Your chat_id is {chat_id}.")


@router.message(Command("add"), F.from_user.id.in_(users))
async def get_start(message: Message, state: FSMContext):
    await message.answer('ок. добавь строку на английском языке')
    # Устанавливаем пользователю состояние "добавляет строку на английском"
    await state.set_state(AddPhrase.add_english)


@router.message(AddPhrase.add_english, F.from_user.id.in_(users))
async def get_cost(message: Message, state: FSMContext):
    if check_english_phrase(message.text.lower()):
        await state.update_data(answer=message.text.lower().replace("'", '"'))
        await message.answer(
            text='ок. теперь добавь перевод на русский язык'

        )
        await state.set_state(AddPhrase.add_russian)
    else:
        await message.answer(
            text='фраза должна быть на английском языке.'

        )


@router.message(AddPhrase.add_russian, F.from_user.id.in_(users))
async def get_category_cost(message: Message, state: FSMContext):
    if check_russian_phrase(message.text.lower()):
        await state.update_data(ask=message.text.lower())
        user_data = await state.get_data()
        await message.answer(
            text=f"добавляем фразу {user_data['answer']} / {user_data['ask']}"
        )
        add_phrases(ask=user_data['ask'], answer=user_data['answer'])
        await state.clear()
    else:
        await message.answer(
            text="фраза должна быть на русском языке"
        )


@router.message(Command("delete"), F.from_user.id.in_(users))
async def get_start(message: Message, state: FSMContext):
    await message.answer('ок. добавь строку на английском языке которую надо удалить')
    # Устанавливаем пользователю состояние "добавляет строку на английском"
    await state.set_state(AddPhrase.delete)


@router.message(AddPhrase.delete, F.from_user.id.in_(users))
async def get_category_cost(message: Message, state: FSMContext):
    if check_english_phrase(message.text.lower()):
        await state.update_data(english=message.text.lower().replace("'", '"'))
        user_data = await state.get_data()
        await message.answer(
            text=f"удалил фразу {user_data['answer']}"
        )
        delete_phrase(user_data['answer'])
        await state.clear()
    else:
        await message.answer(
            text="фраза должна быть на английском языке"
        )


@router.message(Command("today"), F.from_user.id.in_(users))
async def get_start(message: Message):
    quantity = get_quantity_phrases_add_today()
    await message.answer(f'ок. сегодня в БД добавлено фраз: {quantity}')


if __name__ == "__main__":
    pass
