import sqlite3
from crewai.tools import BaseTool


class PlayerScoutTool:
    @staticmethod
    def search_players(position_type: str, filters: dict) -> str:
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

        if filters.get('min_rating'):
            base_query += f" AND rating >= {filters['min_rating']}"
        if filters.get('max_age'):
            base_query += f" AND age <= {filters['max_age']}"
        if filters.get('min_height'):
            base_query += f" AND height >= {filters['min_height']}"
        if filters.get('max_value'):
            base_query += f" AND transferValue <= {filters['max_value']}"

        base_query += " ORDER BY rating DESC LIMIT 8"

        conn = sqlite3.connect('database/data_fute.db')
        cursor = conn.cursor()
        cursor.execute(base_query)
        results = cursor.fetchall()

        output = ""
        for player in results:
            output += (
                f"🔍 **{player[0]}** ({player[1]}) | {player[8]}\n"
                f"- 📊 Rating: {player[4]} | 🎯 G/A: {player[6]}/{player[7]}\n"
                f"- 📏 {player[3]}cm | 🎂 {player[2]} anos\n"
                f"- 💰 Valor: €{player[5]/1_000_000:.2f}M\n"
                f"{'-'*40}\n"
            )
        return output or "Nenhum jogador encontrado com esses critérios"


# ==========================
# TOOLS PERSONALIZADAS
# ==========================

class ScoutGoalkeeper(BaseTool):
    name: str = "ScoutGoleiros"
    description: str = "Busca goleiros com filtros como rating, idade e altura"

    def _run(self, filters: dict) -> str:
        return PlayerScoutTool.search_players("goalkeeper", filters)

class ScoutDefender(BaseTool):
    name: str = "ScoutDefensores"
    description: str = "Busca defensores com filtros como rating, idade e altura"

    def _run(self, filters: dict) -> str:
        return PlayerScoutTool.search_players("defender", filters)
    

class ScoutMidfielder(BaseTool):
    name: str = "ScoutMeioCampistas"
    description: str = "Busca meio-campistas com filtros como rating, idade e altura"

    def _run(self, filters: dict) -> str:
        return PlayerScoutTool.search_players("midfielder", filters)

class ScoutAttacker(BaseTool):
    name: str = "ScoutAtacantes"
    description: str = "Busca atacantes com filtros como rating, idade e altura"

    def _run(self, filters: dict) -> str:
        return PlayerScoutTool.search_players("attacker", filters)


# Instância das ferramentas para uso nos agentes
scout_goalkeeper = ScoutGoalkeeper()
scout_defender = ScoutDefender()
scout_midfielder = ScoutMidfielder()
scout_attacker = ScoutAttacker()























# --------------------------------


# import sqlite3
# from crewai_tools import Tool


# class PlayerScoutTool:
#     @staticmethod
#     def search_players(position_type: str, filters: dict) -> str:
#         """
#         Busca jogadores com filtros dinâmicos
#         Args:
#             position_type: 'defender' | 'midfielder' | 'attacker'
#             filters: dict com critérios (ex: {'min_rating': 6.0, 'max_age': 27})
#         """
#         position_map = {
#             'defender': "role = 'defender_long' AND positionIdsDesc LIKE '%CB%'",
#             'midfielder': "role LIKE '%midfielder%' AND positionIdsDesc LIKE '%CM%'",
#             'attacker': "role LIKE '%forward%' AND positionIdsDesc LIKE '%ST%'"
#         }

#         base_query = f"""
#             SELECT 
#                 name, cname, age, height, rating, transferValue, 
#                 goals, assists, positionIdsDesc
#             FROM players
#             WHERE {position_map[position_type]}
#         """

#         # Construção dinâmica dos filtros
#         if filters.get('min_rating'):
#             base_query += f" AND rating >= {filters['min_rating']}"
#         if filters.get('max_age'):
#             base_query += f" AND age <= {filters['max_age']}"
#         if filters.get('min_height'):
#             base_query += f" AND height >= {filters['min_height']}"
#         if filters.get('max_value'):
#             base_query += f" AND transferValue <= {filters['max_value']}"

#         base_query += " ORDER BY rating DESC LIMIT 5"

#         conn = sqlite3.connect('database/data_fute.db')
#         cursor = conn.cursor()
#         cursor.execute(base_query)
#         results = cursor.fetchall()

#         output = ""
#         for player in results:
#             output += (
#                 f"🔍 **{player[0]}** ({player[1]}) | {player[8]}\n"
#                 f"- 📊 Rating: {player[4]} | 🎯 G/A: {player[5]}/{player[6]}\n"
#                 f"- 📏 {player[3]}cm | 🎂 {player[2]} anos\n"
#                 f"- 💰 Valor: €{player[5]/1000000:.2f}M\n"
#                 f"{'-'*40}\n"
#             )
#         return output or "Nenhum jogador encontrado com esses critérios"

# # Ferramentas instanciadas
# scout_defender = Tool(
#     name="ScoutDefensores",
#     func=lambda filters: PlayerScoutTool.search_players('defender', filters),
#     description="Busca defesas com filtros personalizáveis"
# )

# scout_midfielder = Tool(
#     name="ScoutMeioCampistas",
#     func=lambda filters: PlayerScoutTool.search_players('midfielder', filters),
#     description="Busca meio-campistas com filtros personalizáveis"
# )

# scout_attacker = Tool(
#     name="ScoutAtacantes",
#     func=lambda filters: PlayerScoutTool.search_players('attacker', filters),
#     description="Busca atacantes com filtros personalizáveis"
# )