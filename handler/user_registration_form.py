from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

from config.bot_config import bot
from keyboard.start_menu_keyboard import REGISTER_CALLBACK


class FormStates(StatesGroup):
    nickname = State()
    bio = State()
    age = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send me your nickname, please"
    )
    await FormStates.nickname.set()


def register_registration_handlers(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(registration_start,
                                               lambda call: call.data == REGISTER_CALLBACK)
