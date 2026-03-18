import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =========================
# 1. Carregamento de dados
# =========================
def load_data(path):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


# =========================
# 2. Análise exploratória
# =========================
def basic_info(df):
    print("\n--- Primeiras linhas ---")
    print(df.head())

    print("\n--- Informações do dataset ---")
    df.info()

    print("\n--- Estatísticas ---")
    print(df.describe())


# =========================
# 3. Métricas da fila
# =========================
def analyze_queue_metrics(df):
    queue = df["queue"]

    max_queue = queue.max()
    avg_queue = queue.mean()
    p95 = np.percentile(queue, 95)

    print("\n--- Métricas da Fila ---")
    print(f"Fila máxima: {max_queue}")
    print(f"Fila média: {avg_queue:.2f}")
    print(f"P95 (95% do tempo abaixo de): {p95:.2f}")

    return {
        "max": max_queue,
        "avg": avg_queue,
        "p95": p95
    }


# =========================
# 4. Visualização
# =========================
def plot_queue(df):
    plt.figure(figsize=(10, 5))

    plt.plot(df["timestamp"], df["queue"])

    plt.title("Comportamento da Fila ao Longo do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Itens na fila")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("../data/queue_simulation.png")
    plt.show()

    print("\nGráfico salvo em: data/queue_simulation.png")