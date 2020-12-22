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
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgrespassword")
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
    Column("name", String(50), primary_key=True),
    Column("plot", String(250), primary_key=True),
    Column("genres", ARRAY(String), primary_key=True),
    Column("casts_id", ARRAY(String), primary_key=True),
)

database = Database(DATABASE_URL)
