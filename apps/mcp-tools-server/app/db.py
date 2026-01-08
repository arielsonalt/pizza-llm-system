import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import time
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@postgres:5432/pizza"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def init_db():
    from app import models  # noqa
    Base.metadata.create_all(bind=engine)
    
def init_db():
    from app import models  # noqa

    for _ in range(30):
        try:
            Base.metadata.create_all(bind=engine)
            return
        except OperationalError:
            time.sleep(2)

    raise RuntimeError("Postgres not ready after retries")