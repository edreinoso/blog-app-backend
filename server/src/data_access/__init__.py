import os

import sqlalchemy as sqla

from .models import Base
from .repositories.blogpost_repository import SQLAlchemyBlogPostRepository
from .repositories.users_repository import SQLAlchemyUsersRepository

USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB = os.getenv('POSTGRES_DB')
HOST = os.getenv('POSTGRES_HOST')

engine = sqla.create_engine(
    f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB}",
    echo=os.getenv('ENV') == 'development',
    pool_size=10,
    max_overflow=10)


def init_db():
    Base.metadata.create_all(engine)


user_repository = SQLAlchemyUsersRepository(engine)
blogpost_repository = SQLAlchemyBlogPostRepository(engine)
