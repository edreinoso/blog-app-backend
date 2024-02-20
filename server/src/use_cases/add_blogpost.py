from src.data_access.types import IBlogPostRepository
from src.entities.blogpost import BlogPost, make_blogpost
from typing_extensions import TypedDict


class Input(TypedDict):
    title: str
    content: str


def build_add_blogpost(blogpost_repository: IBlogPostRepository):

    def add_blogpost(user_id: str, data: Input) -> BlogPost:
        blogpost = make_blogpost({**data, 'user_id': user_id})

        blogpost_repository.insert(blogpost)

        return blogpost

    return add_blogpost
