from dto.pill_model import Pill, db_to_pill
from repository.pill_repository import PillRepository


class PillService:
    def __init__(self):
        self.repository = PillRepository()

    async def create_pill(self, pills: list):
        saved_pills = []
        for pill in pills:
            saved_pill = self.repository.insert(pill)
            saved_pills.append(db_to_pill(saved_pill))

        return saved_pills

    async def find_all_pills(self, tg_id):
        pill_list = self.repository.find_by_tg_id(tg_id)
        return [db_to_pill(item) for item in pill_list]
