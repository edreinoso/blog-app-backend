from typing import Optional

from src.data_access.types import IUsersRepository
from src.entities.user import User, make_user
from src.errors import ValidationError
from src.plugins.password_manager.password_manager_interface import \
    IPasswordManager
from typing_extensions import TypedDict


class Input(TypedDict):
    email: str
    password: str
    image: Optional[str]
    first_name: str
    last_name: str


def build_signup(
    users_repository: IUsersRepository,
    password_manager: IPasswordManager
):

    def signup(data: Input) -> User:
        email = data['email'].lower().strip()

        if users_repository.get_user_by_email(email) is not None:
            raise ValidationError("This email is already in use.")

        hashed_password = password_manager.hash_password(data['password'])

        # TODO(andrea): handle the image storage

        user = make_user({**data, 'email': email, 'password': hashed_password})
        users_repository.insert(user)

        return user

    return signup
