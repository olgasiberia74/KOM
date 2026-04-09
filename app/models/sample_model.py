from pydantic import BaseModel, Field


class SampleRequest(BaseModel):
    value: int = Field(..., ge=0, description="Non-negative integer for sample calculation")


class SampleResponse(BaseModel):
    input: int
    output: int
    message: str
