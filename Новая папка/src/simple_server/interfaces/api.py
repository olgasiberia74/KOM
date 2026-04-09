from fastapi import APIRouter
from ..use_cases.get_hello import GetHelloUseCase

router = APIRouter(prefix="/api")

@router.get("/hello")
def get_hello():
    use_case = GetHelloUseCase()
    response = use_case.execute()
    return response.dict()