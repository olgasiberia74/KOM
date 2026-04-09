from typing import List

from fastapi import APIRouter

from app.models.survey_model import Answer, AnswersRequest, AnswersResponse, Question
from app.services.survey_service import SurveyService

router = APIRouter()

@router.get("/questions", response_model=List[Question], summary="Get survey questions")
async def get_questions() -> List[Question]:
    return SurveyService.get_questions()

@router.post("/answers", response_model=AnswersResponse, summary="Submit survey answers")
async def save_answers(payload: AnswersRequest) -> AnswersResponse:
    saved_count = SurveyService.save_answers(payload.answers)
    return AnswersResponse(message="Спасибо! Ваши ответы сохранены.", saved_count=saved_count)
