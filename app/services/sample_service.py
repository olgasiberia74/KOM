from typing import Optional


class SampleService:
    @staticmethod
    def calculate(value: int) -> Optional[int]:
        if value < 0:
            return None
        return value * 2
