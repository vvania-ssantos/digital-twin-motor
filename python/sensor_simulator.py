import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# quantidade de registros simulados
num_registros = 200

# horário inicial
tempo_inicial = datetime.now()

dados = []

fila = 0

for i in range(num_registros):

    timestamp = tempo_inicial + timedelta(seconds=i * 10)

    # itens chegando na esteira
    itens_chegando = np.random.randint(8, 13)

    # itens processados pelo operador
    itens_processados = np.random.randint(7, 12)

    # cálculo da fila
    fila = max(0, fila + itens_chegando - itens_processados)

    # sensores simulados
    temperature = np.random.normal(70, 5)
    vibration = np.random.normal(8, 2)
    speed = np.random.normal(50, 5)
    current = np.random.normal(15, 3)

    # cálculo de falha
    failure_score = 0

    if temperature > 74:
        failure_score += 1

    if vibration > 8.5:
        failure_score += 1

    if current > 16:
        failure_score += 1

    if speed < 49:
        failure_score += 1

    failure = 1 if failure_score >= 2 else 0

    # adiciona os dados na lista
    dados.append({
        "timestamp": timestamp,
        "queue": fila,
        "temperature": round(temperature, 2),
        "vibration": round(vibration, 2),
        "speed": round(speed, 2),
        "current": round(current, 2),
        "failure": failure
    })

# cria dataframe
df = pd.DataFrame(dados)

# garante que a pasta existe
os.makedirs("data", exist_ok=True)

# salva os dados
df.to_csv("data/conveyor_data.csv", index=False)

print("Dados simulados gerados com sucesso!")

print(df["failure"].value_counts())