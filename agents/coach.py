from crewai import Agent
from tools.database_tool import (
    scout_goalkeeper, scout_defender,
    scout_midfielder, scout_attacker
)

coach_agent = Agent(
    role="Técnico Especialista em Formações Táticas",
    goal="Definir os requisitos técnicos ideais para montar um time no esquema 4-3-3 e 4-2-3-1.",
    backstory="Você é o técnico do Paysandu e está focado em encontrar atletas que se encaixem no seu estilo tático e características desejadas por posição.",
    tools=[],  # técnico não usa ferramentas, só raciocina
    verbose=True,
    memory=True,
    allow_delegation=False,
)