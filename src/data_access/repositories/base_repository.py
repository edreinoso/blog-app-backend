import sqlalchemy as sqla


class SQLAlchemyEntityRepository:
    engine: sqla.engine.Engine

    def __init__(self, engine: sqla.engine.Engine):
        self.engine = engine
