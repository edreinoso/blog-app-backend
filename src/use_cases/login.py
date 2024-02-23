from src.data_access.types import IUsersRepository
from src.entities.user import User
from src.errors import AuthorizationError
from src.plugins.password_manager.password_manager_interface import \
    IPasswordManager


def build_login(
    users_repository: IUsersRepository,
    password_manager: IPasswordManager
):

    def login(email: str, password: str) -> User:
        user = users_repository.get_user_by_email(email.lower().strip())

        if user is None:
            # NOTE: this is a deliberately vague error message
            raise AuthorizationError("Wrong email or password.")

        if not password_manager.validate_password(password, user.password):
            # NOTE: this is a deliberately vague error message
            raise AuthorizationError("Wrong email or password.")

        return user

    return login
