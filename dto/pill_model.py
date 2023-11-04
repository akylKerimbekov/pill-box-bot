from aiogram import types


class Pill:
    def __init__(self, pill_id, tg_id, description, time, frequency, is_active):
        self.pill_id = pill_id
        self.tg_id = tg_id
        self.description = description
        self.time = time
        self.frequency = frequency
        self.is_active = is_active

    def __str__(self):
        return (f"Pill id: {self.pill_id}, "
                f"tg_id: {self.tg_id}, "
                f"description: {self.description}, "
                f"time: {self.time}, "
                f"frequency: {self.frequency}, "
                f"is active: {self.is_active}")


def message_to_pill(message: types.Message) -> Pill:
    return Pill(
        pill_id=None,
        tg_id=message.from_user.id,
        description=message.from_user.username,
        time=message.from_user.first_name,
        frequency=message.from_user.last_name,
        is_active=1
    )


def db_to_pill(unit: dict):
    return Pill(
        pill_id=unit["id"],
        tg_id=unit["tg_id"],
        description=unit["description"],
        time=unit["time"],
        frequency=unit["frequency"],
        is_active=unit["is_active"]
    )
