from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///database.db"


engine = create_engine(
    DATABASE_URL,
    echo=True
)


SessionLocal = sessionmaker(
    bind=engine
)


class Base(DeclarativeBase):
    pass


def create_tables():
    Base.metadata.create_all(bind=engine)