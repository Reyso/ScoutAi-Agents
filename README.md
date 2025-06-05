# ⚽ ScoutAI - Sistema Multi-agentes de Scouting de Futebol

![Python](https://img.shields.io/badge/python-3.10%2B-green)
![CrewAI](https://img.shields.io/badge/framework-CrewAI-red)
![SQLite](https://img.shields.io/badge/database-SQLite-blue)
![Pandas](https://img.shields.io/badge/analysis-Pandas-white)

## 👨🏻‍💻 Sobre o Projeto

Projeto desenvolvido para praticar habilidades em:
- **Automação de processos** com multi-agentes inteligentes
- **Análise de dados** sob restrições financeiras
- **Integração entre** critérios técnicos e realidade de mercado

## 📌 Visão Geral

O ScoutAI é um sistema de recomendação de jogadores que combina análise técnica e financeira para auxiliar clubes sul-americanos no mercado de transferências. Através de agentes IA especializados, o sistema:

- Interpreta requisitos táticos do corpo técnico
- Cruza com dados reais de desempenho e valor de mercado
- Recomenda os jogadores que melhor atendem aos critérios dentro do orçamento disponível

## 🏗️ Arquitetura do Sistema

```mermaid
graph LR
    A[Agente Técnico] -->|Define critérios| B[Agente Executivo]
    B -->|Consulta| C[(Banco de Dados)]
    C -->|Retorna dados| B
    B -->|Gera| D[Relatório Tático-Financeiro]
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

# Frameworks e Pacotes
| Tecnologia | Aplicação |
| --- | --- |
| CrewAI | Framework para criação e coordenação dos agentes|
| SQLite | Armazenamento e consulta dos dados de jogadores |

# Fonte de dados
- API Football Data: Estatísticas de desempenho
- Transfermarkt: Valores de mercado e informações complementares

# Saida do sistema
Relatório Gerado (`report.md`):

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

# The end

Projeto desenvolvido por Reyso Teixeira como parte do portfólio em Ciência/Analise de Dados.