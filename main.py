import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Crew
from datetime import datetime

from agents.coach import coach_agent
from agents.executive import executive_agent
from tasks.negotiation import create_coach_task, create_executive_task

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-nano",  
    # model= 'text-embedding-3-small',  
    temperature=0.5,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Criação das tarefas associadas aos agentes
task_coach = create_coach_task(coach_agent)
task_exec = create_executive_task(executive_agent)


# print(task_coach)
# print(task_exec)



crew = Crew(
    agents=[coach_agent, executive_agent],
    tasks=[task_coach, task_exec],
    llm=llm,
    verbose=1,  # Aumente o verboso para ver o processo
    memory=True,  # Ative a memória para compartilhamento de contexto
    process="sequential"  # Os agentes trabalharão em sequência colaborativa
)

result = crew.kickoff()
print(result)


with open("report.md", "w", encoding="utf-8") as f:
    f.write(f"# Relatório da ScoutAI\n")
    f.write(f"_Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}_\n\n")
    f.write("## Resultado:\n\n")
    f.write(str(result))
