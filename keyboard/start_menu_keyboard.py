from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

REGISTER_CALLBACK = "register_tg_user"


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        "Registration",
        callback_data=REGISTER_CALLBACK
    )
    markup.add(registration_button)
    return markup
