import sys
from dotenv import load_dotenv
from agent import create_api_agent

load_dotenv() # Загружает ключ API из файла .env

def main():
    if len(sys.argv) < 2:
        print("Usage: py main.py 'Your request here'")
        return

    user_query = sys.argv[1]
    agent_executor = create_api_agent()
    
    result = agent_executor.invoke({
        "input": user_query,
        "chat_history": []
    })
    
    print("\n--- FINAL RESPONSE ---\n")
    print(result["output"])

if __name__ == "__main__":
    main()
