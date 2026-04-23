import pandas as pd

def verificar_eventos(datas_transacao):
    df = pd.DataFrame({'data': pd.to_datetime(datas_transacao)})
    eventos = {'12-25': 'Natal', '11-27': 'Black Friday'}
    
    df['cod_data'] = df['data'].dt.strftime('%m-%d')
    df['is_evento_comercial'] = df['cod_data'].isin(eventos.keys()).astype(int)
    return df.drop(columns=['cod_data'])

datas = ["2026-05-10", "2026-11-27", "2026-12-25"]
print(verificar_eventos(datas))