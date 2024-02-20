import time
import uuid
from dataclasses import dataclass

from src.entities.unique_entity import UniqueEntity
from src.errors import ValidationError


@dataclass
class BlogPost(UniqueEntity):
    title: str
    content: str
    user_id: str


def make_blogpost(data: dict):
    current_timestamp: int = int(time.time() * 1000)

    id: str = data.get('id', str(uuid.uuid4()))
    created_at: int = data.get('created_at', current_timestamp)
    modified_at: int = data.get('modified_at', current_timestamp)

    if type(id) != str:
        raise ValidationError('A blog post must have a valid id.')

    if type(created_at) != int or created_at > current_timestamp:
        raise ValidationError(
            'A blog post must have a valid creation timestamp.')

    if type(modified_at) != int or modified_at > current_timestamp:
        raise ValidationError(
            'A blog post must have a valid modification timestamp.')

    if 'title' not in data or type(data['title']) != str:
        raise ValidationError('A blog post must have a valid title.')

    if 'content' not in data or type(data['content']) != str:
        raise ValidationError('A blog post must have a valid content.')

    if 'user_id' not in data or type(data['user_id']) != str:
        raise ValidationError('A blog post must have a valid user id.')

    return BlogPost(
        id=id,
        created_at=created_at,
        modified_at=modified_at,
        title=data['title'],
        content=data['content'],
        user_id=data['user_id']
    )
