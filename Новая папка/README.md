# Simple Python Server

A simple Python server built with FastAPI, following clean architecture principles, using uv for dependency management.

## Features

- Clean Architecture: Separated into domain, use cases, interfaces, and infrastructure layers
- FastAPI: Modern, fast web framework for building APIs
- Swagger UI: Automatic API documentation at `/docs`
- uv: Fast Python package installer and resolver

## Project Structure

```
src/
  simple_server/
    domain/          # Business entities and rules
    use_cases/       # Application business logic
    interfaces/      # Controllers and presenters (API routes)
    infrastructure/  # External concerns (databases, frameworks)
    main.py          # Application entry point
```

## Installation

1. Install uv (if not already installed):
   ```bash
   # On Windows PowerShell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

### Development

Run the server with auto-reload:
```bash
uv run uvicorn src.simple_server.main:app --reload
```

Or using the script:
```bash
uv run server
```

### Production

Run the server:
```bash
uv run uvicorn src.simple_server.main:app --host 0.0.0.0 --port 8000
```

## Full-Stack App

This project now includes a minimal frontend and backend.

- `GET /`: Serves the static frontend
- `GET /api/hello`: Returns backend JSON data
- `GET /docs`: Swagger UI for the API

## Project Structure

```
src/
  simple_server/
    domain/
    interfaces/
    infrastructure/
    static/          # Frontend static files
      index.html
      main.js
    use_cases/
    main.py
```

## Usage

### Run the app

```bash
cd 'c:\Users\KOM\python_uv_server\Новая папка'
uv sync
uv run uvicorn src.simple_server.main:app --reload
```

### Open in browser

- Frontend: http://localhost:8000
- API documentation: http://localhost:8000/docs
- API endpoint: http://localhost:8000/api/hello

## Best Practices Applied

- **Clean Architecture**: Separation of concerns with clear layer boundaries
- **Dependency Injection**: Use cases are instantiated in controllers
- **Type Hints**: Full type annotations for better code quality
- **Pydantic Models**: Data validation and serialization
- **uv**: Modern dependency management with pyproject.toml
- **src Layout**: Proper Python package structure