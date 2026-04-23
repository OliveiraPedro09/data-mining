import numpy as np

tempos = [20, 25, 30, 35, 40, 45, 90]

# Quartis com NumPy (Método estatístico padrão)
q1 = np.percentile(tempos, 25)
q2 = np.percentile(tempos, 50)
q3 = np.percentile(tempos, 75)

# Cálculo do IQR e Limites
iqr = q3 - q1
lim_inf = q1 - (1.5 * iqr)
lim_sup = q3 + (1.5 * iqr)

# 2. Verificação Genérica (Exemplo_01_2)
outliers = [t for t in tempos if t < lim_inf or t > lim_sup]

print(f"Q1: {q1} | Q2: {q2} | Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limites: {lim_inf} a {lim_sup}")
print(f"Outliers encontrados: {outliers}")
