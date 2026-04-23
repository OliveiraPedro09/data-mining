import pandas as pd

dados = {
    'Paciente': ['Joana', 'Marcos', 'Criança_A', 'Ricardo', 'Beatriz'],
    'Altura_Metros': [1.65, 180, 0.55, 2.10, 0.15] # 180 (cm) e 0.15 (erro)
}

df = pd.DataFrame(dados)

LIMITE_MIN = 0.40
LIMITE_MAX = 2.50

df_anomalias = df[(df['Altura_Metros'] < LIMITE_MIN) | (df['Altura_Metros'] > LIMITE_MAX)]

print(f"--- Pacientes com Altura Suspeita (Fora de {LIMITE_MIN}m - {LIMITE_MAX}m) ---")
print(df_anomalias)