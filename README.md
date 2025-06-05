# ⚽ ScoutAI - Sistema Multi-agentes de Scouting de Futebol

![Python](https://img.shields.io/badge/python-3.10%2B-green)
![CrewAI](https://img.shields.io/badge/framework-CrewAI-red)
![SQLite](https://img.shields.io/badge/database-SQLite-blue)
![Pandas](https://img.shields.io/badge/analysis-Pandas-white)

## 👨🏻‍💻 Sobre o Projeto


Projeto  desenvolvido para praticar habilidades em automação com agentes inteligentes, tratamento e análise de dados. Simula um sistema  de scouting para clubes sul-americanos.

<!-- - **Critérios táticos** do corpo técnico  
- **Restrições financeiras** da diretoria  
- **Dados reais** de desempenho e mercado -->

## 🚀 Overview

![Image](https://github.com/user-attachments/assets/ef46def7-e9da-477d-8fcf-dd8fbbd829ae)




O ScoutAI é um sistema de recomendação de jogadores que combina análise técnica e financeira para auxiliar clubes sul-americanos no mercado de transferências. Através de agentes IA especializados, o sistema:

- Interpreta requisitos táticos do corpo técnico
- Cruza com dados reais de desempenho e valor de mercado
- Recomenda os jogadores que melhor atendem aos critérios dentro do orçamento disponível

# 📋 Estrutura do Projeto
```bash
ScoutAI-Agents/
├── extract/
│   ├── tabela_times.py # Coleta os time das ligas
│   └── players.py      # Coleta os jogadores dos times 
├── agents/
│   ├── coach.py        # AI Agents Técnico de futebol
│   └── executive.py    # AI Agents Executivo de futebol
├── database/
│   └── data_fute.db    # Banco SQLite
├── tools/
│   └── database_tool.py # Tool para Consultas SQL
├── tasks/
│   └── negotiation.py   # Task para os AI Agents
├── main.py              # Pipeline principal
└── report.md            # Relatório final dos jogadores selecionados             


```


## 👨‍💼 Agentes e seus Papéis
### Agente técnico
Responsabilidade: Traduzir necessidades táticas em critérios mensuráveis

Tomada de Decisão:

- Define atributos ideais por posição (ex.: altura mínima para zagueiros)

- Estabelece níveis de desempenho aceitáveis (rating, gols, assistências)

- Considera características do esquema tático (ex.: Zagueiro com participação ofensiva)

### Agente Executivo
Responsabilidade: Operacionalizar os critérios técnicos dentro de restrições financeiras

Fluxo de Trabalho:

- Recebe os filtros do Agente Técnico;
- Converte em queries SQL otimizadas;
- Aplica camada de análise financeira;
- Gera relatório com as 3 melhores jogadores opções por posição com justificativa;


# Como executar

## 1. Clone o projeto

```bash
git clone https://github.com/Reyso/ScoutAi-Agents.git
cd ScoutAi-Agents
```
## 2. Crie e ative o ambiente virtual

```bash
conda create -n scoutai python=3.10
conda activate scoutai
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```
## 4. Configure a chave da OpenAI
Crie um arquivo `.env` com:
```bash
OPENAI_API_KEY=sk-sua-chave-aqui
```
## 5. Execute o projeto

```
python3 main.py
```

# 📤Saida do sistema  
### ⚠️ Veja o Relatório Final Gerado em (`report.md`)⚠️

```
### 🧤 Goleiro
- **Nome:** Alisson  
  **Idade:** 29  
  **Altura:** 190 cm  
  **Rating:** 8.31  
  **Valor:** €100.000  
- **Justificativa:** Alisson é um goleiro com alto rating e excelente presença na área, ideal para manter a segurança defensiva.

### ⚽ Atacante
- **Nome:** Carlao  
  **Idade:** 32  
  **Altura:** 185 cm  
  **Rating:** 7.27  
  **Valor:** €200.000  
- **Justificativa:** Carlao é um atacante experiente que pode trazer eficácia ao ataque, sempre contribuindo com gols.
...
```

____



# ⚙️ Tecnologias Utilziadas
| Tecnologia | Aplicação |
| --- | --- |
| Python | Scrips e implementação|
| CrewAI | Framework para criação e coordenação de sistemas multiagentes|
| GPT-4.1 nano | Modelo de LLM responsável pela tomada de decisão dos agentes |
| PlayerScoutTool | Tool desenvolvida para conexão e query no banco de dados|
| SQLite | Armazenamento e consulta dos dados de jogadores |



# 🛢 Fonte de dados/ Banco de dados e sua estrutura
Você pode conferir o banco de dados utilziado em `database\data_fute.db` desenvolvido em sqlite3.
### API Football Data
- Estatísticas de desempenho
- Cobertura da Séries A/B/C do Brasil + Ligas Argentina/Bolívia/Paraguai  na temporada de 2025
### Transfermarkt
- Valores de mercado atualizados
### Estrutura do Banco de Dados
 - Tabela "players" com os atributos por jogador

| Atributo          | Descrição                               |
| ----------------- | --------------------------------------- |
| `name`            | Nome do jogador                         |
| `cname`           | País                                    |
| `age`             | Idade                                   |
| `height`          | Altura em cm                            |
| `rating`          | Nota média de performance               |
| `goals`           | Número de gols                          |
| `assists`         | Assistências                            |
| `rcards/ycards`   | Cartões vermelhos/amarelos              |
| `transferValue`   | Valor estimado de mercado (em €)        |
| `positionIdsDesc` | Posições jogadas (ex: CB, ST, CAM, etc) |

---




# 🌐 Contato

Para dúvidas ou colaborações, sinta-se a vontade em me contactar:

- Author: Reyso Teixeira
- GitHub: [Reyso](https://github.com/Reyso)
- LinkedIn: [Reyso Teixeira](https://www.linkedin.com/in/reyso-teixeira/)
- Website: [Pagina de portifólio](https://reyso.github.io/portifolio_projetos)
