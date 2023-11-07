from dto.pill_model import Pill, db_to_pill
from repository.pill_repository import PillRepository


class PillService:
    def __init__(self):
        self.repository = PillRepository()

    async def create_pill(self, pills: list):
        for pill in pills:
            self.repository.insert(pill)

    async def find_all_pills(self, tg_id):
        pill_list = self.repository.find_by_tg_id(tg_id)
        return [db_to_pill(item) for item in pill_list]
