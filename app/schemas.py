from pydantic import BaseModel, Field


class NutritionalValue(BaseModel):
    name: str
    calories: float = Field(alias="ккал")
    proteins: float = Field(alias="белки")
    fats: float = Field(alias="жиры")
    carbs: float = Field(alias="углеводы")
