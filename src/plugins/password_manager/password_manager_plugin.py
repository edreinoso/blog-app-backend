

import bcrypt

from .password_manager_interface import IPasswordManager


class BcryptPasswordManager(IPasswordManager):

    def validate_password(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())\
            .decode('utf-8')
