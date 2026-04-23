import pandas as pd
import numpy as np

dados = {
    'Sensor_ID': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B'],
    'Valor_Leitura': [10, 12, 11, 13, 50, 12, 100, 105, 102, 108, 10, 104]
}
df = pd.DataFrame(dados)

def buscar_outliers_grupo(grupo):
    q1 = grupo.quantile(0.25)
    q3 = grupo.quantile(0.75)
    iqr = q3 - q1
    ls = q3 + 1.5 * iqr
    li = q1 - 1.5 * iqr
    
    return (grupo < li) | (grupo > ls)

df['Eh_Outlier'] = df.groupby('Sensor_ID')['Valor_Leitura'].transform(buscar_outliers_grupo)

anomalias = df[df['Eh_Outlier'] == True]

print("--- DataFrame Completo com Marcação ---")
print(df)
print("\n--- Apenas as Anomalias (Independente por Sensor) ---")
print(anomalias)