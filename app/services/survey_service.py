from typing import List

from app.models.survey_model import Answer, Question


class SurveyService:
    _answers: List[Answer] = []

    _questions: List[Question] = [
        Question(id=1, text="Как вас зовут?"),
        Question(id=2, text="Какой ваш любимый язык программирования?"),
        Question(id=3, text="Чем вы любите заниматься в свободное время?"),
        Question(id=4, text="Сколько часов в день вы учитесь?"),
        Question(id=5, text="В каком городе вы живёте?"),
    ]

    @classmethod
    def get_questions(cls) -> List[Question]:
        return cls._questions

    @classmethod
    def save_answers(cls, answers: List[Answer]) -> int:
        cls._answers.extend(answers)
        return len(cls._answers)

    @classmethod
    def get_all_answers(cls) -> List[Answer]:
        return cls._answers
