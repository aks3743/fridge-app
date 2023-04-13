
import requests
api_key = "6ff24ce729fa45f38f268a74154d3fd3"
base_url = "https://api.spoonacular.com/recipes/findByIngredients"
for product in ['apple','banana','eggs']:
    params = {
        "apiKey": api_key,
        "ingredients": product,
        "number": 3  # Number of recipes to retrieve
    }
    response = requests.get(base_url, params=params)
    recipes = response.json()

for recipe in recipes:
    print(recipe["title"])