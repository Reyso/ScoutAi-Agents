import requests

url = "https://free-api-live-football-data.p.rapidapi.com/football-get-list-player"

querystring = {"teamid":"1626"}

headers = {
	"x-rapidapi-key": "8d31400aa6msh80bbf1ce3eecc9ap1e9d35jsnd45ef4bf0e35",
	"x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())