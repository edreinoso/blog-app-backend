import re
import time
import uuid
from dataclasses import dataclass
from typing import Optional

from src.entities.unique_entity import UniqueEntity
from src.errors import ValidationError


@dataclass
class User(UniqueEntity):
    email: str
    password: str
    first_name: str
    last_name: str
    image_path: Optional[str] = None


def make_user(data: dict):
    current_timestamp: int = int(time.time() * 1000)

    id: str = data.get('id', str(uuid.uuid4()))
    created_at: int = data.get('created_at', current_timestamp)
    modified_at: int = data.get('modified_at', current_timestamp)

    if type(id) != str:
        raise ValidationError('A user must have a valid id.')

    if type(created_at) != int or created_at > current_timestamp:
        raise ValidationError('A user must have a valid creation timestamp.')

    if type(modified_at) != int or modified_at > current_timestamp:
        raise ValidationError(
            'A user must have a valid modification timestamp.')

    if (
        'email' not in data or
        type(data['email']) != str or
        re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            data['email']
        ) is None
    ):
        raise ValidationError('A user must have a valid email.')

    if 'password' not in data or type(data['password']) != str:
        raise ValidationError('A user must have a valid password.')

    if 'first_name' not in data or type(data['first_name']) != str:
        raise ValidationError('A user must have a valid first name.')

    if 'last_name' not in data or type(data['last_name']) != str:
        raise ValidationError('A user must have a valid last name.')

    return User(
        id=id,
        created_at=created_at,
        modified_at=modified_at,
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name']  # NOTE: this is hashed
    )
