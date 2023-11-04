from aiogram import types


class User:
    def __init__(self, user_id, tg_id, username, first_name, last_name, phone_number, is_active):
        self.user_id = user_id
        self.tg_id = tg_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.is_active = is_active


def message_to_user(message: types.Message) -> User:
    return User(
        user_id=None,
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        phone_number="",
        is_active=1
    )


def db_to_user(unit: dict):
    return User(
        user_id=unit["id"],
        tg_id=unit["tg_id"],
        username=unit["username"],
        first_name=unit["first_name"],
        last_name=unit["last_name"],
        phone_number=unit["phone_number"],
        is_active=unit["is_active"]
    )
