import os

DB_USER = os.environ.get("DB_USER", "casts_user")
DB_NAME = os.environ.get("DB_NAME", "casts")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgrespassword")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_ENGINE = os.environ.get("DB_ENGINE", "postgresql")
