

import time
from typing import TypedDict

from src.data_access.models.user import User
from src.data_access.types import IBlogPostRepository, IUsersRepository
from src.entities.blogpost import BlogPost


class Input(TypedDict, total=False):
    cursor: int
    limit: int


def build_list_blogposts(
    blogpost_repository: IBlogPostRepository,
    user_repository: IUsersRepository
):

    def list_blogposts(query: Input) -> tuple[list[BlogPost], list[User], bool]:
        cursor = query.get('cursor', int(time.time()))
        limit = query.get('limit', 25)

        blogposts = blogpost_repository.paginate(cursor, limit + 1)

        users = user_repository.get_all_with_ids(
            [bp.user_id for bp in blogposts])

        return blogposts, users, len(blogposts) == limit + 1

    return list_blogposts
