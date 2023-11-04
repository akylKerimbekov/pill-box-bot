from dto.user_model import User, db_to_user
from repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def create_user(self, user: User):
        if self.not_new_user(tg_id=user.tg_id):
            return user
        saved_user = self.repository.insert(user)
        return db_to_user(saved_user)

    def not_new_user(self, tg_id) -> bool:
        return self.repository.find_by_tg_id(tg_id)
