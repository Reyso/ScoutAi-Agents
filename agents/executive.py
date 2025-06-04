from crewai import Agent
from tools.database_tool import (scout_goalkeeper, scout_defender, 
                               scout_midfielder, scout_attacker)

executive_agent = Agent(
    role="Gerente de Transferências Data-Driven",
    goal="Maximizar o ROI das contratações",
    backstory="""Ex-analista de dados do Manchester City, você desenvolveu modelos próprios
    para prever valorização de jogadores com base em 127 métricas de desempenho.""",
    tools=[scout_goalkeeper, scout_defender, scout_midfielder, scout_attacker],
    verbose=True,
    max_iter=5,
    memory=True,
    # step_callback=lambda x: print(f"Executivo está avaliando: {x.description}")
)