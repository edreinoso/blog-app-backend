from src.data_access.types import IBlogPostRepository
from src.errors import AuthorizationError, ValidationError


def build_remove_blogpost(blogpost_repository: IBlogPostRepository):

    def remove_blogpost(user_id: str, blogpost_id: str):
        blogpost = blogpost_repository.get_by_id(blogpost_id)
        if blogpost is None:
            raise ValidationError("This blog post does not exist.")

        if blogpost.user_id != user_id:
            raise AuthorizationError(
                "You are not authorized to removed this blog post.")

        blogpost_repository.delete(blogpost_id)

    return remove_blogpost
