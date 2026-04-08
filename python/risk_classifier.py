import pandas as pd

def classify_operator_and_set_rpm(processing_time):
    if processing_time > 5:
        perfil = "Iniciante"
        rpm_sugerido = 800
    else:
        perfil = "Veterano"
        rpm_sugerido = 1200
    return perfil, rpm_sugerido

test_data = [6.2, 4.5, 3.8, 7.1]

print(f"{'Tempo (s)':<10} | {'Perfil':<12} | {'RPM Ajustado'}")
print("-" * 40)

for time in test_data:
    perfil, rpm = classify_operator_and_set_rpm(time)
    print(f"{time:<10} | {perfil:<12} | {rpm} RPM")
   