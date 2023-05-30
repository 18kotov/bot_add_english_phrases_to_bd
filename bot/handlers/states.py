from aiogram.fsm.state import StatesGroup, State


class AddPhrase(StatesGroup):
    add_english = State()
    add_russian = State()
    delete = State()
