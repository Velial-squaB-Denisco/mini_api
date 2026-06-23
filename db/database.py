from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config
from sqlalchemy import create_engine

class SqlSession:
    def __init__(self):
        self.engine = create_engine(url=config.DB_URL_SYNC)
        self.SessionLocal = sessionmaker(self.engine)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

sql_session = SqlSession()