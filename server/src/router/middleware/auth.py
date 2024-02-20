from dataclasses import asdict, dataclass
from typing import Optional

from flask_login import LoginManager, current_user
from src.data_access import user_repository
from src.entities.user import User

login_manager = LoginManager()


@dataclass(eq=True)
class FlaskUser:
    id: str
    created_at: str
    modified_at: str
    email: str
    password: str
    first_name: str
    last_name: str
    is_authenticated: bool
    is_anonymous: bool
    is_active: bool = True
    image_path: Optional[str] = None

    def get_id(self) -> str:
        return self.id


def flask_to_internal_user() -> User:
    # NOTE: this should never happen unless this function is misused
    if current_user is None or not current_user.is_authenticated:
        raise RuntimeError("Invalid call. The user must be authenticated")
    return User(
        id=current_user.id,
        created_at=current_user.created_at,
        modified_at=current_user.modified_at,
        email=current_user.email,
        password=current_user.password,
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        image_path=current_user.image_path
    )


@login_manager.user_loader
def load_user(user_id: str) -> FlaskUser:
    user = user_repository.get_by_id(user_id)
    if user is None:
        return None
    return FlaskUser(**asdict(user),
                     is_active=True,
                     is_anonymous=False,
                     is_authenticated=True)
