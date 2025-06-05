import sqlite3
from crewai.tools import BaseTool


class PlayerScoutTool:
    @staticmethod
    def search_players(position_type: str, filters: dict) -> list:
        position_map = {
            'goalkeeper': "role = 'keeper_long' AND positionIdsDesc LIKE '%GK%'",
            'defender': "role = 'defender_long' AND positionIdsDesc LIKE '%CB%'",
            'midfielder': "role LIKE '%midfielder%' AND positionIdsDesc LIKE '%CM%'",
            'attacker': "role LIKE '%attacker%' AND positionIdsDesc LIKE '%ST%'"
        }

        base_query = f"""
            SELECT 
                name, cname, age, height, rating, transferValue,
                goals, assists, positionIdsDesc
            FROM players
            WHERE {position_map[position_type]}
        """

        # Aplicar filtros recebidos
        if filters.get('min_rating'):
            base_query += f" AND rating >= {filters['min_rating']}"
        if filters.get('max_age'):
            base_query += f" AND age <= {filters['max_age']}"
        if filters.get('min_height'):
            base_query += f" AND height >= {filters['min_height']}"
        if filters.get('min_goals'):
            base_query += f" AND goals >= {filters['min_goals']}"
        if filters.get('max_rcards'):
            base_query += f" AND rcards <= {filters['max_rcards']}"
        if filters.get('min_assists'):
            base_query += f" AND assists >= {filters['min_assists']}"
        if filters.get('max_value'):
            base_query += f" AND transferValue <= {filters['max_value']}"

        # Garantir dados válidos
        base_query += " AND transferValue > 0 AND height > 0"
        base_query += " ORDER BY rating DESC LIMIT 5"

        conn = sqlite3.connect('database/data_fute.db')
        cursor = conn.cursor()
        cursor.execute(base_query)
        rows = cursor.fetchall()
        conn.close()

        # Converter para lista de dicionários
        results = []
        for r in rows:
            results.append({
                "nome": r[0],
                "pais": r[1],
                "idade": r[2],
                "altura_cm": r[3],
                "rating": r[4],
                "valor_eur": r[5],
                "gols": r[6],
                "assistencias": r[7],
                "posicoes": r[8]
            })
        return results


# ==========================
# TOOLS PERSONALIZADAS
# ==========================

class ScoutGoalkeeper(BaseTool):
    name: str = "ScoutGoleiros"
    description: str = "Retorna dados de goleiros com base nos filtros técnicos"
    def _run(self, filters: dict) -> list:
        return PlayerScoutTool.search_players("goalkeeper", filters)


class ScoutDefender(BaseTool):
    name: str = "ScoutDefensores"
    description: str = "Retorna dados de zagueiros com base nos filtros técnicos"
    def _run(self, filters: dict) -> list:
        return PlayerScoutTool.search_players("defender", filters)


class ScoutMidfielder(BaseTool):
    name: str = "ScoutMeioCampistas"
    description: str = "Retorna dados de meias com base nos filtros técnicos"
    def _run(self, filters: dict) -> list:
        return PlayerScoutTool.search_players("midfielder", filters)


class ScoutAttacker(BaseTool):
    name: str = "ScoutAtacantes"
    description: str = "Retorna dados de atacantes com base nos filtros técnicos"
    def _run(self, filters: dict) -> list:
        return PlayerScoutTool.search_players("attacker", filters)


# Ferramentas disponíveis para importação
scout_goalkeeper = ScoutGoalkeeper()
scout_defender = ScoutDefender()
scout_midfielder = ScoutMidfielder()
scout_attacker = ScoutAttacker()
