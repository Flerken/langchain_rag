from pydantic import BaseModel, Field


class MultiQueryOutput(BaseModel):
    """
    Список сгенерированных формулировок исходного запроса.
    """
    queries: list[str] = Field(description="Список из 5 различных формулировок исходного запроса")