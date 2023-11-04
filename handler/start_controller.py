from aiogram import types, Dispatcher

from config.bot_config import bot
from dto.user_model import message_to_user
from keyboard.pill_menu_keyboard import pill_keyboard
from service.user_service import UserService


async def start_button(message: types.Message):
    print(message)
    user = message_to_user(message)
    saved_user = await UserService().create_user(user)
    if saved_user and saved_user.user_id:
        response_text = "You have registered successfully"
    else:
        response_text = "You have registered already"

    await bot.send_message(
        chat_id=message.from_user.id,
        text=response_text,
        reply_markup=await pill_keyboard()
    )


def register_start_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start_button, commands=['start'])
