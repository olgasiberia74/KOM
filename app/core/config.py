from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_prefix: str = "/api"
    app_name: str = "python_uv_server"
    debug: bool = True


settings = Settings()

