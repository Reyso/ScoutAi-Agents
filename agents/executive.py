from crewai import Agent
from tools.database_tool import (
    scout_goalkeeper, scout_defender,
    scout_midfielder, scout_attacker
)

executive_agent = Agent(
    role="Executivo de Futebol",
    goal="Analisar os filtros do técnico e gerar um relatório estratégico com os melhores jogadores",
    backstory="""Você é o executivo responsável por contratações. Seu papel é aplicar os critérios do técnico, encontrar atletas dentro das condições ideais e apresentar justificativas técnicas e financeiras para cada nome.""",
    tools=[scout_goalkeeper, scout_defender, scout_midfielder, scout_attacker],
    verbose=True,
    memory=True,
    allow_delegation=False,
)
