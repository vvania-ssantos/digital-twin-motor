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
    fila = max(0, fila + itens_chegando - itens_processados)

    dados.append({
        "timestamp": timestamp,
        "arriving_items": itens_chegando,
        "processed_items": itens_processados,
        "queue": fila
    })

# cria dataframe
df = pd.DataFrame(dados)

# garante que a pasta existe
os.makedirs("data", exist_ok=True)

# salva os dados
df.to_csv("data/conveyor_data.csv", index=False)

print("Dados simulados gerados com sucesso!")

# -----------------------------
# BUSCAR CAPACIDADE IDEAL
# -----------------------------

def simulate_queue(df, capacity):
    queue = 0
    queue_history = []

    for i in range(len(df)):
        arriving = df.loc[i, 'arriving_items']
        processed = min(capacity, queue + arriving)
        queue = queue + arriving - processed
        queue_history.append(queue)

    return queue_history


def find_min_capacity(df, min_cap=8, max_cap=20):
    results = []

    for cap in range(min_cap, max_cap + 1):
        simulated = simulate_queue(df, cap)
        final_queue = simulated[-1]
        results.append((cap, final_queue))

    return results


results = find_min_capacity(df)

print("\nTeste de capacidades:")
for cap, queue in results:
    print(f"Capacidade {cap} → fila final: {queue}")

def simulate_queue(arriving_items, capacity):
    queue = []
    current_queue = 0

    for arriving in arriving_items:
        current_queue += arriving
        processed = min(current_queue, capacity)
        current_queue -= processed
        queue.append(current_queue)

    return queue