from typing import List

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    text: str


class Answer(BaseModel):
    question_id: int
    text: str


class AnswersRequest(BaseModel):
    answers: List[Answer]


class AnswersResponse(BaseModel):
    message: str
    saved_count: int
