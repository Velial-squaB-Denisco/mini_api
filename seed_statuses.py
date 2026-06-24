from sqlalchemy import inspect
from db.database import sql_session
from db.models import Base, Status

INITIAL_STATUSES = [
    {"id": "1", "name": "new", "description": "Новая задача"},
    {"id": "2", "name": "in_progress", "description": "В процессе"},
    {"id": "3", "name": "done", "description": "Завершена"},
]


def seed_statuses():
    Base.metadata.create_all(bind=sql_session.engine)
    
    db = sql_session.SessionLocal()
    try:
        existing_count = db.query(Status).count()
        
        if existing_count > 0:
            return
        
        for status_data in INITIAL_STATUSES:
            status = Status(**status_data)
            db.add(status)
        
        db.commit()
        
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_statuses()