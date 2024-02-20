from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from src.entities.blogpost import BlogPost
from src.entities.user import User

T = TypeVar('T')


class IEntityRepository(Generic[T], ABC):

    @abstractmethod
    def insert(self, obj: T):
        ...

    @abstractmethod
    def delete(self, id: str):
        ...

    @abstractmethod
    def update(self, obj: T):
        ...

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[T]:
        ...

    @abstractmethod
    def get_all_with_ids(self, ids: list[str]) -> list[T]:
        ...

    @abstractmethod
    def paginate(self, cursor: int, limit: int) -> list[T]:
        ...


class IUsersRepository(IEntityRepository[User], ABC):

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        ...


class IBlogPostRepository(IEntityRepository[BlogPost], ABC):
    ...
