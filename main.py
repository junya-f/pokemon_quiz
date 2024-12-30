from fastapi import FastAPI
import requests, random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#id生成する個数の指定。重複のないランダムなIDを生成する
@app.get("/pokemon/quiz")
async def pokemon_quiz():
    ids = random.sample(range(1, 152), 3)
    pokemon_data = []
    base_url = "https://pokeapi.co/api/v2/pokemon"

    for pokemon_id in ids:
        try:
            response = requests.get(f"{base_url}/{pokemon_id}")
            response.raise_for_status()
            data = response.json()
            pokemon_data.append({
                "id": pokemon_id,
                "name": data["name"],
                "image": data["sprites"]["front_default"]
            })
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for ID {pokemon_id}: {e}")

    return {"quiz": pokemon_data}

#テストコード
if __name__ == "__main__":
    print("ランダムなIDを生成中")
    random_ids = generate_random_ids()
    print(f"生成されたID: {random_ids}")
    
    print("APIからポケモンデータを取得中")
    result = fetch_pokemon_data(random_ids)
    print(f"取得結果: {result}")







#APIを叩く練習用に記述
#@app.get("/pokemon/{id}")
#def get_pokemon_data(id: int):
#    #ポケモンAPIへのリクエスト
#    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
#    
#    #ステータスコードの確認
#    if response.status_code == 200:
#        data = response.json()
#        return {
#            "name": data["name"],
#            "image": data["sprites"]["front_default"]
#        }
#    return {"error": "Pokemon not found"}
#ランダムに

#ポケモンAPIから取得したデータをフロントエンドに渡す。処理



#クイズに必要となる情報を取得。画像データと正答となる名前データ。二つはランダムに抽出する
#Jsonデータをフロントエンドに渡す
#API通信が失敗した時の処理