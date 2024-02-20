import sqlalchemy as sqla
from src.data_access.models import Base


class User(Base):
    __tablename__ = 'user'

    id = sqla.Column(sqla.String, primary_key=True)
    created_at = sqla.Column(sqla.BigInteger)
    modified_at = sqla.Column(sqla.BigInteger)

    email = sqla.Column(sqla.String, unique=True)
    password = sqla.Column(sqla.String)

    first_name = sqla.Column(sqla.String)
    last_name = sqla.Column(sqla.String)
    image_path = sqla.Column(sqla.String)

    blogposts = sqla.orm.relationship("BlogPost", back_populates="user")
