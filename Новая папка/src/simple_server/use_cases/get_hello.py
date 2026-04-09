from datetime import datetime
from ..domain.models import HelloResponse

class GetHelloUseCase:
    def execute(self) -> HelloResponse:
        return HelloResponse(
            message="Hello, World!",
            timestamp=datetime.now().isoformat()
        )