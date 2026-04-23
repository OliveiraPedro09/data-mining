import pandas as pd

def analisar_aceleracao_sensor(leituras):
    df = pd.DataFrame(leituras, columns=['leitura'])

    df['delta'] = df['leitura'].diff()
    df['aceleracao'] = df['delta'].diff()
    df['alerta_exponencial'] = (df['aceleracao'] > 0).astype(int)
    
    return df

dados_sensor = [100, 105, 115, 130, 155]

df_resultado = analisar_aceleracao_sensor(dados_sensor)
print(df_resultado)