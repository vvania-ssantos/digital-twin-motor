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