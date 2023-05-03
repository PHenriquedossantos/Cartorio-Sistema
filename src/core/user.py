from src.models.user import User
from src.models.user_db import User as UserDB

from src.database.dbconfig import session

class UserCore:
    def create_user(self, user: User):
        with session:
            new_user = UserDB(**user.dict())
            session.add(new_user)
            session.commit()
            return new_user
        
    def list_users(self):
        with session:
            users = session.query(UserDB).all()
            return users
        
    def delete_user(self, id: str):
        with session:
            user = session.query(UserDB).filter(UserDB.id == id).first()
            if not user:
                return False
            session.delete(user)
            session.commit()
            return True

