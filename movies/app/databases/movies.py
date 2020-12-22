import os

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    ARRAY,
)


from databases import Database

DB_USER = os.environ.get("DB_USER", "movies_user")
DB_NAME = os.environ.get("DB_NAME", "movies")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgresspassword")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_ENGINE = os.environ.get("DB_ENGINE", "postgresql")

DATABASE_URL = (
    f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("plot", String(250)),
    Column("genres", ARRAY(String)),
    Column("casts_id", ARRAY(Integer)),
)

database = Database(DATABASE_URL)
