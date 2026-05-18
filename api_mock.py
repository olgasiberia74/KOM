import uuid

class TaskAPI:
    def __init__(self):
        self.tasks = {} # Имитация базы данных {id: {title, status, desc}}

    def create_task(self, title: str, description: str):
        task_id = str(uuid.uuid4())[:8]
        self.tasks[task_id] = {"title": title, "description": description, "status": "todo"}
        return {"id": task_id, "title": title, "status": "todo"}

    def get_task(self, task_id: str):
        return self.tasks.get(task_id, "Task not found")

    def update_status(self, task_id: str, status: str):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = status
            return {"id": task_id, "new_status": status}
        return {"error": "Task not found"}

    def list_tasks(self):
        return self.tasks

# Создаем один общий объект API, который будут использовать все
api_service = TaskAPI()
