from fastapi import APIRouter, HTTPException
from app.models.sample_model import SampleRequest, SampleResponse
from app.services.sample_service import SampleService

router = APIRouter()

@router.post("/sample", response_model=SampleResponse, summary="Run sample calculation")
async def sample_endpoint(payload: SampleRequest) -> SampleResponse:
    result = SampleService.calculate(payload.value)
    if result is None:
        raise HTTPException(status_code=400, detail="Invalid value")
    return SampleResponse(
        input=payload.value,
        output=result,
        message="Sample endpoint returned a result.",
    )
