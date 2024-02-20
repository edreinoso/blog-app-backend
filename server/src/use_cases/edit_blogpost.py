from dataclasses import asdict
from typing import TypedDict

from src.data_access.types import IBlogPostRepository
from src.entities.blogpost import BlogPost, make_blogpost
from src.errors import AuthorizationError, ValidationError


class Input(TypedDict, total=False):
    title: str
    content: str


def build_edit_blogpost(blogpost_repository: IBlogPostRepository):

    def edit_blogpost(
        user_id: str,
        blogpost_id: str,
        data: Input
    ) -> BlogPost:
        blogpost = blogpost_repository.get_by_id(blogpost_id)
        if blogpost is None:
            raise ValidationError("This blog post does not exists.")

        if blogpost.user_id != user_id:
            raise AuthorizationError(
                "You are not authorized to edit this blog post.")

        updated_blogpost = make_blogpost({**asdict(blogpost), **data})

        blogpost_repository.update(updated_blogpost)

        return updated_blogpost

    return edit_blogpost
