from fastapi import FastAPI
from enum import Enum
app = FastAPI()


@app.get("/")
async def hello():
    return {'hello': 'home'}


@app.get("/hello/{name}")
async def hello_person(name: str):
    return {'hello': name}

class AvailableCuisines (str, Enum) :
    indian = "indian"
    american = "american"
    italian = "italian"

food_items = {
    'indian': ["Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple pie"],
    'italian': ["Ravioli", "pizza"]
}
valid_cuisines = food_items.keys()

# @app.get("/get_items/{cuisine}")
# async def get_items(cuisine):

#     if cuisine not in valid_cuisines:
#         return f"Supported cuisines are {valid_cuisines}"

#     return food_items. get(cuisine)


@app.get("/get_items/{cuisine}")
async def get_items(cuisine:AvailableCuisines):

    return food_items. get(cuisine)

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount': coupon_code.get(code) }