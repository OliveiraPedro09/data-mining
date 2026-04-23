import pandas as pd

def calcular_razao_comprometimento(dados):
    df = pd.DataFrame(dados)
    df['razao_comprometimento'] = df['divida_total'] / df['renda_mensal']
    
    return df

dados_clientes = {
    'cliente': ['A', 'B', 'C'],
    'renda_mensal': [10000, 2000, 5000],
    'divida_total': [3000, 1500, 1000]
}

df_resultado = calcular_razao_comprometimento(dados_clientes)
print(df_resultado)