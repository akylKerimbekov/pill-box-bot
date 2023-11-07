from datetime import time

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from config.bot_config import bot
from dto.pill_model import Pill
from dto.user_model import message_to_user
from keyboard.pill_menu_keyboard import NEW_PILL_CALLBACK, LIST_PILL_CALLBACK
from service.pill_service import PillService
from service.user_service import UserService


class PillRegisterStates(StatesGroup):
    description = State()
    time = State()
    frequency = State()


async def new_pill_start(call: types.CallbackQuery):
    print("new pill")
    user = message_to_user(call.message)
    await UserService().create_user(user)
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Description",
    )
    await PillRegisterStates.description.set()


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send time, please"
    )
    await PillRegisterStates.next()


async def load_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if 'times' not in data:
            data['times'] = []
        try:
            if message.text.lower() == 'done':
                await bot.send_message(chat_id=message.from_user.id, text="Send frequency, please.")
                await PillRegisterStates.next()
            else:
                pill_time = time.fromisoformat(message.text)
                data['times'].append(pill_time.isoformat())
                await message.answer("Time added. Send me another time or type 'done' to continue.")
                await PillRegisterStates.time.set()
        except ValueError:
            await message.answer("Sorry, incorrect time format. Please use 'HH:MM'.")
            return


async def load_frequency(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["frequency"] = "every day"
        pills = []
        for item in data["times"]:
            pills.append(Pill(None, message.from_user.id, data["description"], item, data["frequency"], 1))
        await PillService().create_pill(pills)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Registered successfully"
    )
    await state.finish()


async def list_pill(call: types.CallbackQuery):
    pills = await PillService().find_all_pills(call.from_user.id)
    for pill in pills:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Pill: {pill.description} : {pill.time}"
        )


def register_pill_form_handlers(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(new_pill_start,
                                               lambda call: call.data == NEW_PILL_CALLBACK)
    dispatcher.register_callback_query_handler(list_pill,
                                               lambda call: call.data == LIST_PILL_CALLBACK)
    dispatcher.register_message_handler(load_description,
                                        state=PillRegisterStates.description,
                                        content_types=["text"])
    dispatcher.register_message_handler(load_time,
                                        state=PillRegisterStates.time)
    dispatcher.register_message_handler(load_frequency,
                                        state=PillRegisterStates.frequency)
