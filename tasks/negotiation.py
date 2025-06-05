from crewai import Task

def create_coach_task(agent):
    return Task(
        name="coach_task",
        description="""Defina filtros técnicos para cada posição com os seguintes critérios rigorosos:

1. **Goleiro**: 
   - Rating >=6.0
   - Altura >190cm 
   - Valor máximo: €300.000 (transferValue < 300000)

2. **Zagueiro**: 
   - Altura >=185cm
   - Rating >5.6
   - Gols >=1
   - Valor máximo: €400.000 (transferValue < 400000)

3. **Meia**: 
   - Rating >6.5
   - Cartões vermelhos <2
   - Assistências >=2
   - Valor máximo: €450.000 (transferValue < 450000)

4. **Atacante**: 
   - Rating >6.9
   - Gols >3
   - Valor máximo: €500.000 (transferValue < 500000)
   - Idade <34 anos

Retorne um dicionário com esses filtros no formato:
{
    'keeper': {'min_rating': 6.0, 'min_height': 190, 'max_value': 300000},
    'defender': {'min_rating': 5.6, 'min_height': 185, 'min_goals': 1, 'max_value': 400000},
    'midfielder': {'min_rating': 6.5, 'max_rcards': 2, 'min_assists': 2, 'max_value': 450000},
    'attacker': {'min_rating': 6.9, 'min_goals': 3, 'max_value': 500000, 'max_age': 33}
}""",
        expected_output="Dicionário completo com todos os filtros técnicos e financeiros por posição.",
        agent=agent
    )


def create_executive_task(agent):
    return Task(
        name="executive_task",
        description="""USE ESTRITAMENTE os filtros definidos pelo técnico, especialmente os valores máximos de transferência.
NÃO SUGIRA JOGADORES ACIMA DOS VALORES ESTIPULADOS:
- Goleiro: €300k
- Zagueiro: €400k 
- Meia: €450k
- Atacante: €500k



REQUISITOS OBRIGATÓRIOS:
- Listar EXATAMENTE 3 opções por posição
- Priorizar jogadores que atendam TODOS os critérios
- Ordenar por rating (maior primeiro)

Formato esperado:
### 🧤 Goleiro
- Nome, idade, altura, rating, valor...
- Justificativa

### 🛡️ Zagueiro


""",
        expected_output="Relatório com jogadores que atendem TODOS os critérios, incluindo os financeiros.",
        agent=agent,
        context=[create_coach_task(agent)]
    )