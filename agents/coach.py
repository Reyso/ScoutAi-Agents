from crewai import Agent
from tools.database_tool import (scout_goalkeeper, scout_defender, 
                               scout_midfielder, scout_attacker)

coach_agent = Agent(
    role="Técnico Especialista em Formações Táticas",
    goal="Montar um time equilibrado para o sistema 4-3-3",
    backstory="""Você é um técnico que domina análise de desempenho por posição específica.
    Sabe exatamente que atributos são essenciais para cada role no seu sistema de jogo.""",
    tools=[scout_goalkeeper, scout_defender, scout_midfielder, scout_attacker],
    verbose=True,
    memory=True,
    max_iter=7,
    allow_delegation=False,
    # step_callback=lambda x: print(f"Técnico está analisando: {x.description}")
)