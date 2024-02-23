import sqlalchemy as sqla
from src.data_access.models import Base


class BlogPost(Base):
    __tablename__ = 'blogpost'

    id = sqla.Column(sqla.String, primary_key=True)
    created_at = sqla.Column(sqla.BigInteger)
    modified_at = sqla.Column(sqla.BigInteger)

    title = sqla.Column(sqla.String)
    content = sqla.Column(sqla.String)

    user_id = sqla.Column(sqla.String, sqla.ForeignKey('user.id'))
    user = sqla.orm.relationship("User", back_populates="blogposts")
