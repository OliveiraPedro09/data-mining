import pandas as pd

dados = {
    'Item': ['Monitor', 'Teclado Mechanical', 'Cabo HDMI', 'Processador i9', 'Pasta Térmica'],
    'Data_Compra': ['2024-01-10', '2024-01-12', '2024-01-15', '2024-01-20', '2024-01-25'],
    'Data_Entrega': ['2024-01-15', '2024-01-11', '2024-01-16', '2024-01-18', '2024-01-27']
}

df = pd.DataFrame(dados)

df['Data_Compra'] = pd.to_datetime(df['Data_Compra'])

df['Data_Entrega'] = pd.to_datetime(df['Data_Entrega'])
erros_logicos = df[df['Data_Entrega'] < df['Data_Compra']]

print("--- Relatório de Auditoria: Entregas Antecipadas (Erros) ---")
print(erros_logicos)