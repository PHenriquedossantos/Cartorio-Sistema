from src.database.dbconfig import session
from src.errors.user_not_found_exception import UserNotFoundException
from src.models.update_user import UpdateUser
from src.models.user import User
from src.models.user_db import User as UserDB


class UserCore:
    def create_user(self, user: User) -> UserDB:
        with session:
            user.password = UserDB.hash_password(user.password)
            new_user = UserDB(**user.dict())
            session.add(new_user)
            session.commit()
            return new_user

    def list_users(self) -> list[User]:
        with session:
            users = session.query(UserDB).all()
            return users

    def delete_user(self, id: str) -> bool:
        with session:
            user = session.query(UserDB).filter(UserDB.id == id).first()
            if not user:
                return False
            session.delete(user)
            session.commit()
            return True

    def update_user(self, id: str, update_user: UpdateUser) -> UserDB:
        with session:
            user = session.query(UserDB).filter(UserDB.id == id).first()

            if not user:
                raise UserNotFoundException

            for key, value in update_user.dict().items():
                if value:
                    setattr(user, f"{key}", value)

            session.commit()

            return user
