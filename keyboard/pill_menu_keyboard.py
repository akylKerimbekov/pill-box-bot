from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

NEW_PILL_CALLBACK = "new_pill"
LIST_PILL_CALLBACK = "list_all_pills"


async def pill_keyboard():
    markup = InlineKeyboardMarkup()
    new_pill_button = InlineKeyboardButton(
        "New pill",
        callback_data=NEW_PILL_CALLBACK
    )
    list_pill_button = InlineKeyboardButton(
        "List my pills",
        callback_data=LIST_PILL_CALLBACK
    )
    markup.add(new_pill_button)
    markup.add(list_pill_button)
    return markup
