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
    #model="gpt-4.1-nano",  
     model= 'text-embedding-3-small',  
    temperature=0.5,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Criação das tarefas associadas aos agentes
task_coach = create_coach_task(coach_agent)
task_exec = create_executive_task(executive_agent)


crew = Crew(
    agents=[coach_agent, executive_agent],
    tasks=[task_coach, task_exec],
    llm=llm,
    verbose=1,  # Aumente o verboso para ver o processo
    memory=True,  # Ative a memória para compartilhamento de contexto
    process="sequential",  # Os agentes trabalharão em sequência colaborativa
    context_sharing=True
)



# Executa a crew
result = crew.kickoff()



# Gera markdown formatado
now = datetime.now().strftime("%d/%m/%Y %H:%M")
header = f"# 📝 Relatório Técnico de Reforços - ScoutAI\n"
header += f"_Gerado em: {now}_\n\n"
header += "Este relatório foi produzido pela equipe de agentes da ScoutAI.\n"
header += "Ele contém sugestões de reforços com base em critérios técnicos e financeiros definidos pela comissão técnica e diretoria.\n\n"
header += "---\n"

# Salva no arquivo markdown
with open("report.md", "w", encoding="utf-8") as f:
    f.write(header)
    f.write("## 📊 Análise e Justificativas por Posição\n\n")
    f.write(str(result))

print("✅ Relatório salvo em report.md")