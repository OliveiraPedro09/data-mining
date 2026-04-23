import pandas as pd

df = pd.read_csv('dados_sensores.csv')

ausentes = df.isna().sum()
print("--- Quantidade de dados ausentes ---")
print(ausentes)

mediana_temp = df['temperatura_celsius'].median()
mediana_pressao = df['pressao_psi'].median()

df['temperatura_celsius'] = df['temperatura_celsius'].fillna(mediana_temp)
df['pressao_psi'] = df['pressao_psi'].fillna(mediana_pressao)

print("\n--- Pós-tratamento (Check de NaNs) ---")
print(df.isna().sum())

print("\n--- Primeiras linhas do DataFrame tratado ---")
print(df.head())