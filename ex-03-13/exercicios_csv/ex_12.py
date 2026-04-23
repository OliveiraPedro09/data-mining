import pandas as pd

df = pd.read_csv('dados_sensores.csv')
df['temperatura_celsius'] = df['temperatura_celsius'].fillna(df['temperatura_celsius'].median())
df['pressao_psi'] = df['pressao_psi'].fillna(df['pressao_psi'].median())

def obter_limites(coluna):
    q1 = coluna.quantile(0.25)
    q3 = coluna.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

li_temp, ls_temp = obter_limites(df['temperatura_celsius'])
li_pres, ls_pres = obter_limites(df['pressao_psi'])

filtro_temp = (df['temperatura_celsius'] >= li_temp) & (df['temperatura_celsius'] <= ls_temp)
filtro_pres = (df['pressao_psi'] >= li_pres) & (df['pressao_psi'] <= ls_pres)

df_validado = df[filtro_temp & filtro_pres]

df_validado.to_csv('dados_validados.csv', index=False)

print(f"Processamento concluído!")
print(f"Linhas originais: {len(df)}")
print(f"Linhas validadas (sem outliers): {len(df_validado)}")
print(f"Arquivo 'dados_validados.csv' gerado com sucesso.")