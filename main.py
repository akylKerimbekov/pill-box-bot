from aiogram import executor

from config.bot_config import dispatcher
from handler.start_controller import register_start_handlers
from handler.pill_controller import register_pill_form_handlers
from repository.db_manager import DBManager


async def on_startup(_):
    db = DBManager()
    db.init_db()

register_start_handlers(dispatcher=dispatcher)
register_pill_form_handlers(dispatcher=dispatcher)

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dispatcher,
        skip_updates=True,
        on_startup=on_startup
    )
