import numpy as np

tempos = [20, 25, 30, 35, 40, 45, 90]

# 1. Cálculo dos Quartis (Usando NumPy)
q1, q2, q3 = np.percentile(tempos, [25, 50, 75])

# 2. Cálculo do IQR e Limites
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# 3. Verificação Genérica de Outliers (Funciona para qualquer tamanho)
outliers = [t for t in tempos if t < limite_inferior or t > limite_superior]

print(f"--- Resultados NumPy ---")
print(f"Q1: {q1} | Q2: {q2} | Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limites: [{limite_inferior} até {limite_superior}]")
print(f"Outliers detectados: {outliers}")