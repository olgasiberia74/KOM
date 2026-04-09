# Python UV Server

A minimal clean architecture Python server using FastAPI and Uvicorn.

## Features

- Clean project layout with `app`, `api`, `core`, `services`, and `models`
- Built-in Swagger UI at `/docs`
- Sample POST endpoint at `/api/sample`
- VS Code debugging support via `.vscode/launch.json`

## Installation

```powershell
cd python_uv_server
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run server

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open the app at:

- `http://127.0.0.1:8000/`

Open the Swagger UI at:

- `http://127.0.0.1:8000/docs`

## Mini-анкета

- `GET /api/questions` — возвращает список вопросов.
- `POST /api/answers` — принимает ответы и сохраняет их в памяти.
- Фронтенд доступен по `http://127.0.0.1:8000/`.

## Sample request

```powershell
curl -X POST "http://127.0.0.1:8000/api/sample" -H "Content-Type: application/json" -d '{"value": 5}'
```

Response:

```json
{
  "input": 5,
  "output": 10,
  "message": "Sample endpoint returned a result."
}
```

## Run tests

```powershell
pytest
```

## Сдача проекта

Проект готов к сдаче. Для этого:

1. Создайте новый публичный репозиторий на GitHub (или другом git-хостинге).
2. Добавьте remote origin:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/mini-anketa.git
   git push -u origin master
   ```
3. Сделайте скриншоты работы приложения:
   - Главная страница с анкетой (`http://127.0.0.1:8000/`)
   - Страница после отправки (сообщение "Спасибо!")
   - Swagger UI (`http://127.0.0.1:8000/docs`)
   - Результаты тестов (`pytest`)
4. Добавьте скриншоты в папку `screenshots/` и закоммитьте.
5. Ссылка на репозиторий будет вашей сдачей проекта.

Использованные промпты сохранены в `PROMPTS.md`.

