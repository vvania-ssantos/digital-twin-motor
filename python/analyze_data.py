import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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
# 4. Visualização da fila
# =========================
def plot_queue(df):
    plt.figure(figsize=(10, 5))

    plt.plot(df["timestamp"], df["queue"])

    plt.title("Comportamento da Fila ao Longo do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Itens na fila")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("data/queue_simulation.png")
    plt.close()

    print("\nGráfico salvo em: data/queue_simulation.png")


# =========================
# 5. Gráficos adicionais
# =========================
def plot_temperature(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["temperature"], label="Temperatura")

    plt.title("Temperatura ao Longo do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Temperatura (°C)")

    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("data/temperature_over_time.png")
    plt.close()

    print("Gráfico salvo em: data/temperature_over_time.png")


def plot_vibration(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["vibration"], label="Vibração")

    plt.title("Vibração ao Longo do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Vibração")

    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("data/vibration_over_time.png")
    plt.close()

    print("Gráfico salvo em: data/vibration_over_time.png")


def plot_temperature_histogram(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df["temperature"], bins=20)

    plt.title("Distribuição da Temperatura")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frequência")

    plt.tight_layout()
    plt.savefig("data/temperature_histogram.png")
    plt.close()

    print("Gráfico salvo em: data/temperature_histogram.png")


def plot_correlation_heatmap(df):
    plt.figure(figsize=(8, 6))

    numeric_columns = df.select_dtypes(include=[np.number])

    sns.heatmap(numeric_columns.corr(), annot=True, cmap="coolwarm")

    plt.title("Correlação entre Variáveis")
    plt.tight_layout()

    plt.savefig("data/correlation_heatmap.png")
    plt.close()

    print("Gráfico salvo em: data/correlation_heatmap.png")


# =========================
# 6. Execução principal
# =========================
if __name__ == "__main__":
    path = "data/conveyor_data.csv"

    df = load_data(path)

    basic_info(df)
    analyze_queue_metrics(df)

    plot_queue(df)
    plot_temperature(df)
    plot_vibration(df)
    plot_temperature_histogram(df)
    plot_correlation_heatmap(df)