import sqlite3
import requests
import time

# Configuração da API
API_URL = "https://free-api-live-football-data.p.rapidapi.com/football-get-list-player"
HEADERS = {
    "x-rapidapi-key": "8d31400aa6msh80bbf1ce3eecc9ap1e9d35jsnd45ef4bf0e35",
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

# Conexão com o banco
conn = sqlite3.connect("data_fute.db")
cursor = conn.cursor()

# Criação da tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT,
    cname TEXT,
    role TEXT,
    positionId INTEGER,
    rating REAL,
    goals INTEGER,
    assists INTEGER,
    rcards INTEGER,
    ycards INTEGER,
    positionIdsDesc TEXT,
    height REAL,
    age INTEGER,
    transferValue TEXT,
    team_id INTEGER
)
''')
def save_players_for_team(team_id):
    url = "https://free-api-live-football-data.p.rapidapi.com/football-get-list-player"
    params = {"teamid": str(team_id)}

    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()

    if data.get("status") != "success":
        print(f"Erro ao buscar jogadores do time {team_id}")
        return

    squads = data.get("response", {}).get("list", {}).get("squad", [])

    if not squads:
        print(f"Nenhum jogador encontrado para o time {team_id}.")
        return
    
    players_salvos = 0  

    for squad in squads:
        members = squad.get("members", [])
        for player in members:
            try:
                cursor.execute('''
                    INSERT OR REPLACE INTO players (
                        id, name, cname, role, positionId, rating, goals, assists, 
                        rcards, ycards, positionIdsDesc, height, age, transferValue, team_id
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    player.get("id"),
                    player.get("name"),
                    player.get("cname"),
                    player.get("role", {}).get("key") if player.get("role") else None,
                    player.get("positionId"),
                    player.get("rating"),
                    player.get("goals"),
                    player.get("assists"),
                    player.get("rcards"),
                    player.get("ycards"),
                    player.get("positionIdsDesc"),
                    player.get("height"),
                    player.get("age"),
                    player.get("transferValue"),
                    team_id
                ))
                players_salvos += 1
            except Exception as err:
                print(f"Erro ao salvar jogador: {player.get('name')} | {err}")

    if players_salvos:
        print(f"✅ {players_salvos} jogadores do time {team_id} salvos.")
    else:
        print(f"⚠️ Nenhum jogador encontrado para o time {team_id}.")

    print(f"Jogadores do time {team_id} salvos.")

# Lê os times do banco
cursor.execute("SELECT id FROM teams")
team_ids = cursor.fetchall()

# Percorre cada time e salva os jogadores
for (team_id,) in team_ids:
    save_players_for_team(team_id)
    time.sleep(1.3)  # evita sobrecarga na API

conn.commit()
conn.close()