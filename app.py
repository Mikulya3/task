from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import List

app = FastAPI()

class Store(BaseModel):
    id: str
    name: str
    logo_url: HttpUrl
    delivery_type: str
    delivery_time: str
    external_url: HttpUrl

@app.get("/api/v1/stores", response_model=List[Store])
def get_stores():
    return [
        {
            "id": "metro",
            "name": "METRO",
            "logo_url": "https://example.com/logo/metro.png",
            "delivery_type": "scheduled",
            "delivery_time": "today 21:00-23:00",
            "external_url": "https://online.metro-ru",
        },
        {
            "id": "auchan",
            "name": "Ашан",
            "logo_url": "https://cdn.example.com/logos/auchan.png",
            "delivery_type": "scheduled",
            "delivery_time": "today 18:00-20:00",
            "external_url": "https://www.auchan.ru",
        },
        {
            "id": "vkusvill",
            "name": "ВкусВилл",
            "logo_url": "https://cdn.example.com/logos/vkusvill.png",
            "delivery_type": "express",
            "delivery_time": "20-60 minutes",
            "external_url": "https://vkusvill.ru",
        },
        {
            "id": "victoria",
            "name": "Виктория",
            "logo_url": "https://cdn.example.com/logos/victoria.png",
            "delivery_type": "scheduled",
            "delivery_time": "today 17:00-19:00",
            "external_url": "https://victoria-group.ru",
        }
    ]


