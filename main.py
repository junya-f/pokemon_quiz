from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#ポケモンの名前とポケモンのidを取得
@app.get("/pokemon/{id}")
def get_pokemon(id: int):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{id}")
    if response.status_code == 200:
        data = requests.json()
        return {
            "name": data["name"],
            "image": data["sprites"]["front_default"]
        }
    return {"error" "Pokemon not found"}