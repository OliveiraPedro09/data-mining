import pandas as pd

dados = {
    'Componente': ['Resistor 10k', 'Capacitor 100uF', 'LED Vermelho', 'Transistor BC548', 'Protoboard'],
    'Quantidade_Estoque': [150, -20, 45.5, 0, 12] 
}

df = pd.DataFrame(dados)

erro_negativo = df['Quantidade_Estoque'] < 0
erro_fracionado = df['Quantidade_Estoque'] % 1 != 0

df_falhas = df[erro_negativo | erro_fracionado].copy()

print("--- Relatório de Erros de Integridade de Estoque ---")
if df_falhas.empty:
    print("Todos os dados estão matematicamente consistentes.")
else:
    print(df_falhas)