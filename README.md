# 🏭 Digital Twin - Esteira de Produção Inteligente
> Projeto de simulação e análise de dados para otimização de fluxo industrial.

## 🎯 Objetivo do Projeto
Este Digital Twin simula o comportamento de uma esteira industrial, focando na análise de gargalos e no ajuste dinâmico de velocidade (RPM) baseado no perfil do operador. 

## 🧠 O Diferencial: Regras de Negócio & IA
Diferente de uma automação simples, este sistema utiliza **Classificação (Mineração de Dados)** para identificar o ritmo de trabalho:
- **Operador Iniciante:** O sistema detecta maior tempo de processamento e sugere um RPM reduzido para evitar acúmulo na fila (gargalo).
- **Operador Veterano:** O sistema identifica alta eficiência e permite um aumento no RPM para maximizar o throughput.

## 📈 Principais Insights Obtidos
- **Capacidade 10:** Fluxo insuficiente, gera acúmulo crítico.
- **Capacidade 12:** Estabiliza o sistema, mas exige monitoramento de picos de vibração/calor.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem:** Python (Pandas, NumPy, Matplotlib)
- **Ambiente:** WSL 2 (Ubuntu) no VS Code
- **Conceitos:** Data Mining, Simulação de Sensores, Engenharia de Dados.