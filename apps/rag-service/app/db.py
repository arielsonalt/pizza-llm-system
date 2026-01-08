import os
from sqlalchemy import create_engine

def get_db_url() -> str:
    return os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@postgres:5432/pizza"
    )

engine = create_engine(get_db_url(), pool_pre_ping=True)
