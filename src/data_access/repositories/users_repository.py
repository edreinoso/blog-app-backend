from dataclasses import asdict
from typing import Optional

from sqlalchemy.orm import Session
from src.data_access.models.user import User as UserModel
from src.data_access.models.utils import model_to_dict
from src.data_access.types import IUsersRepository
from src.entities.user import User, make_user

from .base_repository import SQLAlchemyEntityRepository


class SQLAlchemyUsersRepository(SQLAlchemyEntityRepository, IUsersRepository):

    def insert(self, obj: User):
        with Session(self.engine) as session:
            record: UserModel = UserModel(**asdict(obj))
            session.add(record)
            session.commit()

    def get_by_id(self, id: str) -> Optional[User]:
        with Session(self.engine) as session:
            record = session.query(UserModel).get(id)
            return make_user(model_to_dict(record)) if record is not None else None

    def get_user_by_email(self, email: str) -> Optional[User]:
        with Session(self.engine) as session:
            record: UserModel = session.query(UserModel)\
                .filter_by(email=email)\
                .first()
            return make_user(model_to_dict(record)) if record is not None else None

    def update(self, obj: User):
        raise NotImplementedError()

    def delete(self, id: str):
        raise NotImplementedError()

    def paginate(self, cursor: int, limit: int) -> list[User]:
        raise NotImplementedError()

    def get_all_with_ids(self, ids: list[str]) -> list[User]:
        with Session(self.engine) as session:
            records = session.query(UserModel)\
                .filter(UserModel.id.in_(ids))\
                .all()
            return [make_user(model_to_dict(record))
                    for record in records]
