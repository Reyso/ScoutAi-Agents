# from crewai import Task

# def create_coach_task(agent):
#     return Task(
#         description="""Defina os requisitos técnicos para:
#         1. **Zagueiro**: Altura >185cm, rating >5.6, bom passe (assists >1)
#         2. **Volante**: Rating >6.5, disciplinado (rcards <2)
#         3. **Atacante**: Rating >6.9, gols >3 , Barato (transferValue < 450000) """,
#         agent=agent,
#         expected_output="""Critérios formatados como dict para cada posição. Exemplo:
#         {'defender': {'min_height': 185, 'min_rating': 5.6, 'min_assists': 1}}"""
#     )

# def create_executive_task(agent):
#     return Task(
#         description="""Converta os critérios técnicos em buscas realistas considerando:
#         - Orçamento máximo: €10M por jogador
#         - Idade preferida: 22-28 anos
#         - Valor de revenda potencial""",
#         agent=agent,
#         expected_output="""Lista de jogadores com:
#         - Nome, idade, valor
#         - Adequação aos critérios (%)
#         - Projeção de valor futuro"""
#     )


from crewai import Task

def create_coach_task(agent):
    return Task(
        description="""Defina requisitos TÁTICOS para:
        1. **Goleiro**: Saída de bola (rating >=6.0) e altura >190cm
        2. **Zagueiro**: Altura >=185cm, rating >5.6, faça gols (goals >=1)
        3. **Meia**: Rating >6.5, disciplinado (rcards <2), bom passe (assists >=1)
        4. **Atacante**: Rating >6.9, gols >3 , Barato (transferValue < 500000)""",
        agent=agent,
        expected_output="""
        - Uma  justificativa pela escolha dos jogadores
        
        - Dicionário com filtros técnicos por posição. Exemplo:
        {
            'keeper': {'min_rating': 6.0, 'min_height': 190},
            'defender': {'min_rating': 5.6, 'min_goals': 1},
            'midfield': {'min_rating': 6.5, max_rcards:2},
            'attacker':{'min_rating': 6.9, 'min_goals':2, 'max_value':500000}
        }"""
    )

def create_executive_task(agent):
    return Task(
        description="""Converta os requisitos táticos em BUSCAS REALISTAS considerando:
        - Valor máximo por posição: Goleiro (300000), Defensor (400000), Meia (460000), Atacante (550000)
        - Idade ideal por posição: Goleiro (28-32), Defensor (24-30), Meia (23-33), Atacante (21-34)
        - Evitar jogadores com >3 cartões vermelhos na temporada""",
        agent=agent,
        expected_output="""Relatório financeiro por posição contendo:
        - Top 3 opções por posição
        - Custo total estimado
        - Projeção de valorização em 3 anos
        - Descrever brevemente justificativa por cada atleta . 
        """
    )