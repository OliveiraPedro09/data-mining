import pandas as pd

dados = {
    'ID_Maquina': [1, 2, 3, 4, 5], 
    'Uso_Memoria_MB': [2048, 2100, 2050, 8192, 2080]
}

df = pd.DataFrame(dados)

q1 = df['Uso_Memoria_MB'].quantile(0.25)
q3 = df['Uso_Memoria_MB'].quantile(0.75)

# IQR (Interquartile Range)
iqr = q3 - q1

print(f"DataFrame:\n{df}\n")
print(f"Percentil 0.25 (Q1): {q1} MB")
print(f"Percentil 0.75 (Q3): {q3} MB")
print(f"IQR (Intervalo Interquartílico): {iqr} MB")