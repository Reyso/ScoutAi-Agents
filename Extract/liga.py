import requests

url = "https://free-api-live-football-data.p.rapidapi.com/football-get-list-player"

querystring = {"teamid":"1626"}

headers = {
	"x-rapidapi-key": "API KEY",
	"x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())