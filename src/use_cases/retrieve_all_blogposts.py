from src.data_access.types import IBlogPostRepository
from src.entities.blogpost import BlogPost


def build_retrieve_all_blogposts(blogpost_repository: IBlogPostRepository):

    def retrieve_blogpost() -> list[BlogPost]:
        return blogpost_repository.get_all()

    return retrieve_blogpost
