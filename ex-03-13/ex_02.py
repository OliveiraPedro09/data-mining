import numpy as np

tempos = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]
q1, q3 = np.percentile(tempos, [25, 75])

# IQR (Interquartile Range)
iqr = q3 - q1

# Limites Inferior e Superior (constante 1.5)
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"IQR: {iqr}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")