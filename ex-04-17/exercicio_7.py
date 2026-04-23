import pandas as pd
import numpy as np

def tratar_nulos_com_indicador(dados):
    df = pd.DataFrame(dados, columns=['leitura_sensor'])
    df['omissao_flag'] = df['leitura_sensor'].isna().astype(int)
    mediana = df['leitura_sensor'].median()
    df['leitura_sensor'] = df['leitura_sensor'].fillna(mediana)
    
    return df

dados_exemplo = [10.2, np.nan, 10.5, 11.0, np.nan, 10.8]

df_resultado = tratar_nulos_com_indicador(dados_exemplo)
print(df_resultado)