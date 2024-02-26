from src.data_access.models.user import User
from src.data_access.types import IBlogPostRepository, IUsersRepository
from src.entities.blogpost import BlogPost


def build_retrieve_all_blogposts(
    blogpost_repository: IBlogPostRepository,
    user_repository: IUsersRepository
):

    def retrieve_blogpost() -> tuple[list[BlogPost], list[User]]:
        blogs = blogpost_repository.get_all()
        
        users = user_repository.get_all_with_ids(
            [bp.user_id for bp in blogs])
        
        return blogs, users

    return retrieve_blogpost
