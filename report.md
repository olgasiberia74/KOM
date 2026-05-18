# Отчёт по выполнению домашнего задания: LangChain API Agent

## 1. Описание проекта
Данный проект представляет собой LLM-агента, который позволяет управлять системой задач через естественный язык. Агент интерпретирует намерения пользователя и вызывает соответствующие методы API через инструменты (Tools) LangChain. Для обеспечения стабильной работы на легкой локальной модели реализован собственный класс-обертка для управления вызовами инструментов.

## 2. Технический стек
- **LLM Провайдер:** Локальный (Ollama).
- **Используемая модель:** `llama3.2:1b` (выбрана для обеспечения работы на устройствах с ограниченным объемом оперативной памяти).
- **Фреймворк:** LangChain.
- **Язык программирования:** Python 3.12.
- **API:** Реализован Mock API (имитация базы данных задач) внутри проекта (`api_mock.py`).

## 3. API и поддерживаемые операции
Для работы агента реализован внутренний сервис `TaskAPI`, поддерживающий следующие операции:
1. `manage_task_create`: Создание новой задачи (заголовок, описание).
2. `manage_task_get`: Получение информации о задаче по её уникальному ID.
3. `manage_task_update`: Изменение статуса задачи (например, на 'done').
4. `manage_task_list`: Получение списка всех созданных задач.

## 4. Инструкция по запуску
Для запуска агента необходимо выполнить следующие шаги:

1. **Установка Ollama:** Скачайте и установите Ollama с сайта [ollama.com](https://ollama.com).
2. **Загрузка модели:**
   ```bash
   ollama run llama3.2:1b


   3. Создание виртуального окружения и установка зависимостей:
py -m venv venv
venv\Scripts\pip install langchain langchain-community langchain-core langchain-ollama python-dotenv

4.Запуск агента из CLI:

venv\Scripts\python main.py "Ваш запрос здесь"

5. Тестирование (Результаты выполнения)
"Создай задачу 'Купить хлеб'"-manage_task_create---- FINAL RESPONSE ---


Status: success
Action: Create task
Data: {'id': '92a96b48', 'title': 'Купить хлеб', 'status': 'todo'}
Errors: none

"Что у меня сейчас в списке задач?"	----manage_task_list------ FINAL RESPONSE ---

Status: success
Action: manage_task_list
Data: [
  {
    "task_id": "12345",
    "description": "This is a task description.",
    "status": "Not Started"
  },
  {
    "task_id": "67890",
    "title": "Another Task Title",
    "description": "This is another task description.",
    "status": "In Progress"
  }
]

Errors: none


"Измени статус задачи [92a96b48] на done"	---- manage_task_update-------- FINAL RESPONSE ---

Here is the function call with its proper arguments:

```json
{
  "name": "manage_task_update",
  "parameters": {
    "task_id": "92a96b48",
    "status": "done"
  }
}
```

Status: success
Action: update
Data: {"kwargs":{"type":"object"},"status":{"value":"done","description":""}}

"Привет! Кто ты и что умеешь?"------------- Status: success, Action: created a task (модель продемонстрировала галлюцинацию, попытавшись вызвать tool вместо простого ответа)

6. Использованные промпты
Системный промпт (System Prompt)
Для настройки роли и соблюдения формата ответа использовался следующий промпт:

You are a helpful assistant. Your only job is to manage tasks using tools.

Instructions:
1. If the user wants to create, list, or update a task, use the appropriate tool.
2. After using the tool, answer in this format:
Status: success
Action: <what you did>
Data: <result>
Errors: none

Шаблоны пользовательских запросов
Агент поддерживает запросы на естественном языке. Примеры:

"Создай задачу [название] с описанием [текст]"
"Что у меня в списке задач?"
"Обнови статус задачи [id] на [статус]"

## 7. Техническое подтверждение (Compliance)

- **Реализация API-tool:** 
  - Объявление инструментов и реальный вызов функций API реализованы в файле `agent.py` в диапазоне строк **L7–L25**.
  - Каждый инструмент вызывает соответствующие методы класса `TaskAPI` из файла `api_mock.py`.
- **Дебаг-логирование:** 
  - Для подтверждения вызова инструментов в файл `agent.py` добавлены `print()` операторы в каждой функции инструмента (строки **L9, L14, L19, L24**). При запуске в консоли отображается сообщение `DEBUG: Calling ...`.
- **Интерпретация запросов:**
  - Пример: Запрос *"Измени статус задачи 92a96b48 на done"* $\rightarrow$ Агент верно интерпретирует намерение и вызывает метод `manage_task_update`.
- **Контракт ответа:**
  - Требования к формату (Status, Action, Data, Errors) жестко закреплены в системном промпте в файле `agent.py` (раздел `self.system_prompt`).
- **Безопасность:**
  - Секреты не закоммичены. В проекте используется локальная модель Ollama, не требующая API-ключей.

