from dto.pill_model import Pill
from repository.db_manager import DBManager
from repository.script import sql_pill_script


class PillRepository:

    def __init__(self):
        self.connection = DBManager().get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "tg_id": row[1],
            "description": row[2],
            "time": row[3],
            "frequency": row[4],
            "is_active": row[5],
        }

    def insert(self, pill: Pill):
        saved_pill = self.cursor.execute(
            sql_pill_script.INSERT_INTO_PILL_QUERY,
            {
                "id": None,
                "tg_id": pill.tg_id,
                "description": pill.description,
                "time": pill.time,
                "frequency": pill.frequency,
                "is_active": pill.is_active
            }
        ).fetchone()
        self.connection.commit()
        return saved_pill

    def find_by_tg_id(self, tg_id):
        saved_pill = self.cursor.execute(
            sql_pill_script.SELECT_ALL_PILLS_BY_TG_ID_QUERY,
            {
                "tg_id": tg_id
            }
        ).fetchall()
        return saved_pill
