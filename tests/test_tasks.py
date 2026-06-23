import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from db.database import sql_session
from db.models import Base, Task

TASK_ID = 1
TEST_DB_URL = "sqlite:///./tasks.db"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[sql_session.get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def cleanup_db():
    db = TestingSessionLocal()
    try:
        db.query(Task).delete()
        db.commit()
        yield
    finally:
        db.close()
        
@pytest.fixture
def task_id():
    response = client.post("/tasks", json={
        "title": "Test task",
        "description": "Desc"
    })
    assert response.status_code == 200
    return response.json()["id"]

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Test task",
        "description": "Desc"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test task"
    assert data["status"] == "new"

def test_change_status(task_id):
    response = client.patch(f"/tasks/{task_id}/status", json={
        "status": "done"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "done"

def test_delete_task(task_id):
    """Тест удаления задачи"""
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200