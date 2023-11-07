from dto.user_model import User
from repository.db_manager import DBManager
from repository.script import sql_user_script


class UserRepository:

    def __init__(self):
        self.connection = DBManager().get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "tg_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "phone_number": row[5],
            "is_active": row[6],
        }

    def insert(self, user: User):
        self.cursor.execute(
            sql_user_script.INSERT_INTO_USER_QUERY,
            {
                "id": None,
                "tg_id": user.tg_id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "is_active": user.is_active
            }
        )
        self.connection.commit()


    def find_by_tg_id(self, tg_id):
        saved_user = self.cursor.execute(
            sql_user_script.SELECT_USER_BY_TG_ID_QUERY,
            {
                "tg_id": tg_id
            }
        ).fetchone()
        return saved_user
