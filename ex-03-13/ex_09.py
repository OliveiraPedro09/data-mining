import pandas as pd
import numpy as np

# 1. Criação do DataFrame com o erro de leitura (300)
df = pd.DataFrame({'Temperatura': [80, 82, 85, 81, 300, 83]})

# 2. Cálculo dos Quartis e Mediana (Q2)
q1 = df['Temperatura'].quantile(0.25)
q3 = df['Temperatura'].quantile(0.75)
mediana = df['Temperatura'].median() # Q2
iqr = q3 - q1

# 3. Definição do Limite Superior
limite_superior = q3 + 1.5 * iqr

# 4. Utilizando np.where(condição, valor_se_verdadeiro, valor_se_falso)
# Se o valor for maior que o limite, substitui pela mediana; caso contrário, mantém o original.
df['Temperatura_Corrigida'] = np.where(
    df['Temperatura'] > limite_superior, 
    mediana, 
    df['Temperatura']
)

# Exibição dos resultados
print(f"Mediana calculada: {mediana}")
print(f"Limite Superior: {limite_superior}")
print("\n--- DataFrame Resultante ---")
print(df)