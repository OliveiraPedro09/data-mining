import pandas as pd
import numpy as np

dados = {
    'ID_Sensor': [101, 102, 103, 104, 105],
    'Temperatura_C': ['23.5', '24.1', 'falha_sinal', '22.8', 'erro_conexao']
}

df = pd.DataFrame(dados)

df['Temperatura_C_Numerica'] = pd.to_numeric(df['Temperatura_C'], errors='coerce')

falhas = df[df['Temperatura_C_Numerica'].isna()]

print("--- Registros com falha na telemetria ---")
print(falhas[['ID_Sensor', 'Temperatura_C']])