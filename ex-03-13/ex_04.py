import numpy as np

tensoes = [110, 115, 120, 118, 112, 220, 116, 114, 119, 12]

# Quartis e IQR
q1, q3 = np.percentile(tensoes, [25, 75])
iqr = q3 - q1

# Limites (Constante 1.5)
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

anomalos = []
for t in tensoes:
    if t < limite_inferior or t > limite_superior:
        anomalos.append(t)

print(f"Limites de normalidade: {limite_inferior}V até {limite_superior}V")
print(f"Valores anômalos detectados: {anomalos}")