import queue
import sqlite3

from config.bot_config import DB_PATH, DB_POOL_MAX_SIZE
from repository.script import sql_user_script, sql_pill_script


class DBManager:
    __instance = None
    database = DB_PATH
    max_size = DB_POOL_MAX_SIZE
    pool = queue.Queue(DB_POOL_MAX_SIZE)

    def __new__(cls, *args, **kwargs):
        cls.__instance = super(DBManager, cls).__new__(cls)
        cls.__instance.pool = queue.Queue(cls.max_size)
        for _ in range(cls.max_size):
            cls.__instance.pool.put(cls.__instance.create_new_connection())

        return cls.__instance

    def create_new_connection(self):
        conn = sqlite3.connect(self.database)
        return conn

    def get_connection(self) -> sqlite3.Connection:
        return self.pool.get()

    def return_connection(self, conn):
        self.pool.put(conn)

    def close_all_connections(self):
        while not self.pool.empty():
            conn = self.pool.get_nowait()
            conn.close()

    def init_db(self):
        self.get_connection().execute(sql_user_script.CREATE_USER_TABLE)
        self.get_connection().execute(sql_pill_script.CREATE_PILL_TABLE)
        print("Database was initiated successfully")
