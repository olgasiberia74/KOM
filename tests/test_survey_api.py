from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_questions_returns_list():
    response = client.get("/api/questions")
    assert response.status_code == 200
    questions = response.json()
    assert isinstance(questions, list)
    assert len(questions) >= 3
    assert questions[0]["id"] == 1


def test_post_answers_saves_data():
    payload = {
        "answers": [
            {"question_id": 1, "text": "Тестовое имя"},
            {"question_id": 2, "text": "Python"},
        ]
    }
    response = client.post("/api/answers", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Спасибо! Ваши ответы сохранены."
    assert response.json()["saved_count"] >= 2
