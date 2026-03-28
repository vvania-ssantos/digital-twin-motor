from analyze_data import load_data, basic_info, analyze_queue_metrics, plot_queue

# caminho do dataset
df = load_data("../data/conveyor_data.csv")

# exploração inicial
basic_info(df)

# métricas
metrics = analyze_queue_metrics(df)

print("\nResumo das métricas:")
print(metrics)

# gráfico
plot_queue(df)