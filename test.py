import requests

# Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your actual Edamam API credentials
api_id = 'c54e8ce4'
api_key = 'e7ec0cc0c7a38c5b63eb6221b2570b49'

# Edamam API endpoint for recipe search
api_url = 'https://api.edamam.com/search'

search_term = input("Enter a search term for recipes: ")
# Example query parameters for searching recipes containing 'chicken'
params = {
    'q': search_term,
    'app_id': api_id,
    'app_key': api_key,
}

# Make the API request
response = requests.get(api_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract and print relevant information from the response
    for hit in data.get('hits', []):
        recipe = hit.get('recipe', {})
        print(recipe.get('label'))
        print(recipe.get('source'))
        print(recipe.get('url'))
else:
    print(f"Error: {response.status_code} - {response.text}")
