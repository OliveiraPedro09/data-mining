import numpy as np

def detectar_anomalias(dados, multiplicador):
    q1, q3 = np.percentile(dados, [25, 75])
    
    # IQR (Interquartile Range)
    iqr = q3 - q1
    
    # Limites com base no multiplicador recebido
    limite_inferior = q1 - multiplicador * iqr
    limite_superior = q3 + multiplicador * iqr
    
    outliers = [valor for valor in dados if valor < limite_inferior or valor > limite_superior]
    
    return outliers

medicoes = [110, 115, 120, 118, 112, 220, 116, 114, 119, 12]
resultado = detectar_anomalias(medicoes, 1.5)

print(f"Anomalias detectadas: {resultado}")