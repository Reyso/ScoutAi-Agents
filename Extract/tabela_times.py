import sqlite3
import requests

# IDs das ligas
league_ids = [268, 8814, 8971,131,144]
# BrSerieA, BrSerieB, BrasileiroSerieC, PePrimeiraDiv,BoPrimeiraDiv

headers = {
    "x-rapidapi-key": "5e20a9969bmsh8783b60f65b59dap196468jsn9eaaaaab524e",
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

# Cria conexão com SQLite
conn = sqlite3.connect("football.db")
cursor = conn.cursor()

# Cria tabela de times
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name TEXT,
        short_name TEXT,
        league_id INTEGER,
        played INTEGER,
        wins INTEGER,
        draws INTEGER,
        losses INTEGER,
        scores_str TEXT,
        goal_con_diff INTEGER,
        pts INTEGER,
        position INTEGER,
        logo_url TEXT
    )
''')

# Função para buscar e salvar times por liga
def save_teams_by_league(league_id):
    url = "https://free-api-live-football-data.p.rapidapi.com/football-get-list-all-team"
    response = requests.get(url, headers=headers, params={"leagueid": str(league_id)})
    data = response.json()
    teams = data.get("response", {}).get("list", [])

    for team in teams:
        print(f"Inserindo time: {team.get('name')}")
        cursor.execute('''
            INSERT OR REPLACE INTO teams VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            team.get("id"),
            team.get("name"),
            team.get("shortName"),
            league_id,
            team.get("played"),
            team.get("wins"),
            team.get("draws"),
            team.get("losses"),
            team.get("scoresStr"),
            team.get("goalConDiff"),
            team.get("pts"),
            team.get("idx"),
            team.get("logo")
        ))
    print(f"✅ Liga {league_id} processada com sucesso.")

# Executa para todas as ligas
for lid in league_ids:
    save_teams_by_league(lid)

conn.commit()
conn.close()
