import numpy as np

def detectar_anomalias(dados, multiplicador):
    q1, q3 = np.percentile(dados, [25, 75])
    iqr = q3 - q1
    
    limite_inferior = q1 - multiplicador * iqr
    limite_superior = q3 + multiplicador * iqr
    
    outliers = [valor for valor in dados if valor < limite_inferior or valor > limite_superior]
    return outliers

vetor_teste = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]

anomalias_encontradas = detectar_anomalias(vetor_teste, 1.5)

print(f"Vetor Original: {vetor_teste}")
print(f"Anomalias detectadas: {anomalias_encontradas}")