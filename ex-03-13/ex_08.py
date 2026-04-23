import pandas as pd

dados = {
    'ID_Maquina': [1, 2, 3, 4, 5], 
    'Uso_Memoria_MB': [2048, 2100, 2050, 8192, 2080]
}
df = pd.DataFrame(dados)

q1 = df['Uso_Memoria_MB'].quantile(0.25)
q3 = df['Uso_Memoria_MB'].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

mascara = (df['Uso_Memoria_MB'] >= limite_inferior) & (df['Uso_Memoria_MB'] <= limite_superior)
df_normal = df[mascara]

print(f"Limites de Normalidade: {limite_inferior} até {limite_superior}")
print("\n--- DataFrame Original ---")
print(df)
print("\n--- DataFrame de Operação Normal (Sem Anomalias) ---")
print(df_normal)