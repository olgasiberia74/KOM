from langchain.tools import tool
from langchain_ollama import ChatOllama 
from langchain_core.prompts import ChatPromptTemplate
from api_mock import api_service
import json
import re
import inspect

# --- Определение инструментов ---
# Теперь все аргументы имеют значение None по умолчанию, чтобы избежать ошибок Python
# --- Определение инструментов ---
@tool
def manage_task_create(title=None, description=None, **kwargs):
    """Создает новую задачу в системе. Аргументы: title (заголовок), description (описание)."""
    print(f"DEBUG: Calling manage_task_create with title={title}") # ДОБАВЛЕНО ДЛЯ ДЕБАГА
    if not title: return "Error: Title is required"
    return api_service.create_task(title, description or "")

@tool
def manage_task_get(task_id=None, **kwargs):
    """Получает информацию о задаче по её ID. Аргумент: task_id."""
    print(f"DEBUG: Calling manage_task_get with id={task_id}") # ДОБАВЛЕНО ДЛЯ ДЕБАГА
    if not task_id: return "Error: Task ID is required"
    return api_service.get_task(task_id)

@tool
def manage_task_update(task_id=None, status=None, **kwargs):
    """Обновляет статус задачи. Аргументы: task_id, status."""
    print(f"DEBUG: Calling manage_task_update with id={task_id}, status={status}") # ДОБАВЛЕНО ДЛЯ ДЕБАГА
    if not task_id or not status: return "Error: Both task_id and status are required"
    return api_service.update_status(task_id, status)

@tool
def manage_task_list(**kwargs):
    """Возвращает список всех существующих задач."""
    print("DEBUG: Calling manage_task_list") # ДОБАВЛЕНО ДЛЯ ДЕБАГА
    return api_service.list_tasks()


class SimpleAgent:
    def __init__(self):
        self.llm = ChatOllama(model="llama3.2:1b", temperature=0)
        self.llm_with_tools = self.llm.bind_tools(tools_list)
        
        self.system_prompt = (
            "You are a helpful assistant. Your only job is to manage tasks using tools."
            "\n\nInstructions:"
            "\n1. If the user wants to create, list, or update a task, use the appropriate tool."
            "\n2. After using the tool, answer in this format:"
            "\nStatus: success"
            "\nAction: <what you did>"
            "\nData: <result>"
            "\nErrors: none"
        )

    def invoke(self, inputs):
        user_input = inputs.get("input")
        messages = [("system", self.system_prompt), ("human", user_input)]
        
        response = self.llm_with_tools.invoke(messages)
        
        tool_call = None
        if response.tool_calls:
            tool_call = response.tool_calls[0]
        else:
            json_match = re.search(r'\{.*\}', response.content, re.DOTALL)
            if json_match:
                try:
                    data = json.loads(json_match.group())
                    if "name" in data:
                        tool_call = {"name": data["name"], "args": data.get("parameters", data.get("args", {}))}
                except:
                    pass

        if tool_call:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            
            if tool_name in tools_map:
                try:
                    func = tools_map[tool_name]
                    if isinstance(tool_args, list):
                        sig = inspect.signature(func)
                        arg_names = list(sig.parameters.keys())
                        # Убираем **kwargs из списка имен
                        arg_names = [n for n in arg_names if n != 'kwargs']
                        tool_args = {name: tool_args[i] for i, name in enumerate(arg_names) if i < len(tool_args)}
                    
                    result = func(**tool_args)
                    prompt_for_final = f"Tool result: {result}. Now provide the final response in the STRICT format: Status, Action, Data, Errors."
                    final_response = self.llm.invoke(messages + [response, ("system", prompt_for_final)])
                    return {"output": final_response.content}
                except Exception as e:
                    return {"output": f"Status: error\nAction: Tool call failed\nData: none\nErrors: {str(e)}"}
        
        return {"output": response.content}

def create_api_agent():
    return SimpleAgent()
