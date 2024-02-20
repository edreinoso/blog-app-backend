from src.data_access.types import IBlogPostRepository
from src.entities.blogpost import BlogPost


def build_retrieve_blogpost(blogpost_repository: IBlogPostRepository):

    def retrieve_blogpost(id: str) -> BlogPost:
        return blogpost_repository.get_by_id(id)

    return retrieve_blogpost
