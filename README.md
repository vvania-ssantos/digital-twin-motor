# 🤖 Digital Twin - Esteira de Produção Inteligente

Projeto focado na simulação e análise do fluxo de produção industrial utilizando conceitos de Digital Twin, monitoramento de sensores e análise preditiva.

---

## 🎯 Objetivo

Este projeto simula o comportamento de uma esteira de produção industrial, monitorando variáveis como:

- Temperatura
- Vibração
- Corrente elétrica
- Velocidade da esteira
- Tamanho da fila

O objetivo é identificar gargalos, detectar anomalias e apoiar tomadas de decisão preventivas antes que falhas operacionais aconteçam.

---

## 🧠 Principais Funcionalidades

- Simulação de sensores industriais
- Ajuste automático da velocidade da esteira
- Análise de filas e detecção de gargalos
- Monitoramento de temperatura e vibração
- Lógica de detecção de anomalias
- Preparação para previsão de falhas com Machine Learning
- Visualização de dados por meio de gráficos e mapas de calor

---

## 🏗️ Estrutura do Projeto

```text
Digital-Twin-Motor/
│
├── data/
│   └── conveyor_data.csv
│
├── images/
│   ├── correlation_heatmap.png
│   ├── queue_simulation.png
│   ├── temperature_histogram.png
│   ├── temperature_over_time.png
│   └── vibration_over_time.png
│
├── notebooks/
│   └── digital_twin_analysis.ipynb
│
├── python/
│   ├── analyze_data.py
│   ├── anomaly_detection.py
│   ├── dashboard.py
│   ├── failure_prediction.py
│   ├── main.py
│   ├── risk_classifier.py
│   └── sensor_simulator.py
│
├── requirements.txt
├── README.md
└── LICENSE

🛠️ Tecnologias Utilizadas
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook / Google Colab
VS Code
Git e GitHub
WSL Ubuntu
📊 Análises Atuais

Atualmente, o projeto inclui:

Análise temporal de temperatura e vibração
Histograma de distribuição de temperatura
Heatmap de correlação entre variáveis
Simulação de filas e análise de gargalos
Classificação inicial de risco operacional
🚨 Lógica de Detecção de Anomalias

O projeto utiliza regras de negócio para classificar situações de risco.

Exemplos:

Temperatura elevada
Vibração excessiva
Fila muito grande
Alto consumo de corrente elétrica

Essas condições podem indicar possíveis falhas operacionais ou necessidade de manutenção preventiva.

🔮 Melhorias Futuras

Próximos passos planejados:

Modelo preditivo de falhas com Machine Learning
Modelos Random Forest e Logistic Regression
Análise de importância das variáveis
Dashboard em tempo real
Integração com SQL para armazenamento dos dados
Versão com dashboard em Streamlit
▶️ Como Executar

Clone o repositório:

git clone https://github.com/vvania-ssantos/digital-twin-motor.git

Acesse a pasta:

cd digital-twin-motor

Crie e ative o ambiente virtual:

python -m venv venv
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Execute o simulador:

python python/sensor_simulator.py

Execute a análise:

python python/analyze_data.py
📌 Status do Projeto

Projeto em evolução contínua, com foco em manutenção preditiva, monitoramento industrial e desenvolvimento de portfólio técnico.

👩‍💻 Autora

Desenvolvido por Vania Santos.