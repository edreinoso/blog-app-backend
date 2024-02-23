from abc import ABC, abstractmethod


class IPasswordManager(ABC):

    @abstractmethod
    def validate_password(self, password: str, hashed: str) -> bool:
        ...

    @abstractmethod
    def hash_password(self, password: str) -> bytes:
        ...
