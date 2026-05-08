from fastapi import FastAPI
import json
from difflib import get_close_matches
from typing import List, Dict
from .schemas import NutritionalValue

app = FastAPI()

FOODS_CACHE: Dict[str, NutritionalValue] = {}


def read_db():
    try:
        with open("app/foods.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


@app.on_event("startup")
async def startup_event():
    raw_data = read_db()

    for item in raw_data:
        for name, info in item.items():
            food_obj = NutritionalValue(name=name, **info)
            FOODS_CACHE[name] = food_obj

    print(f"Готово! Загружено {len(FOODS_CACHE)} позиций.")


@app.get("/search", response_model=List[NutritionalValue])
async def search_food(q: str):
    x = get_close_matches(q, list(FOODS_CACHE.keys()), cutoff=0.1)
    y = [FOODS_CACHE[name] for name in x]

    return y
