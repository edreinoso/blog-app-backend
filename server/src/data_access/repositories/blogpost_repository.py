
from dataclasses import asdict
from typing import Optional

from sqlalchemy.orm import Session
from src.data_access.models.blogpost import BlogPost as BlogPostModel
from src.data_access.models.utils import model_to_dict
from src.data_access.types import IBlogPostRepository
from src.entities.blogpost import BlogPost, make_blogpost

from .base_repository import SQLAlchemyEntityRepository


class SQLAlchemyBlogPostRepository (
    SQLAlchemyEntityRepository,
    IBlogPostRepository
):

    def insert(self, obj: BlogPost) -> None:
        with Session(self.engine) as session:
            return_post = BlogPostModel(**asdict(obj))
            session.add(return_post)
            session.commit()

    def delete(self, post_id: str) -> None:
        print('delete function called', post_id)
        with Session(self.engine) as session:
            session.query(BlogPostModel)\
                .filter_by(id=post_id)\
                .delete(synchronize_session=False)
            session.commit()

    def update(self, obj: BlogPost) -> Optional[BlogPost]:
        with Session(self.engine) as session:
            record: BlogPostModel = session.query(
                BlogPostModel).filter_by(id=obj.id)
            record.one().title = obj.title
            record.one().content = obj.content
            session.commit()

    def get_by_id(self, id: str) -> Optional[BlogPost]:
        with Session(self.engine) as session:
            record: BlogPostModel = session.query(BlogPostModel).get(id)
            return make_blogpost(model_to_dict(record)) if record is not None else None

    def get_all(self) -> list[BlogPost]:
        with Session(self.engine) as session:
            records: List[BlogPostModel] = session.query(BlogPostModel).all()
            return [make_blogpost(model_to_dict(record)) for record in records]
            """records = session.query(BlogPostModel).all()
            print(records)
            return [make_blogpost(model_to_dict(record) for record in records)]"""

    def paginate(self, cursor: int, limit: int) -> list[BlogPost]:
        with Session(self.engine) as session:
            records = session.query(BlogPostModel)\
                .filter(BlogPostModel.created_at <= cursor)\
                .limit(limit)\
                .all()
            return [make_blogpost(model_to_dict(record))
                    for record in records]

    def get_all_with_ids(self, ids: list[str]) -> list[BlogPost]:
        raise NotImplementedError()
