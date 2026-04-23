import pandas as pd
from datetime import datetime

ano_atual = datetime.now().year

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
    'Ano_Nascimento': [2010, 2005, 2012, 1998, 2015],
    'Idade_Declarada': [16, 21, 14, 28, 9] 
}

df = pd.DataFrame(dados)

df['Idade_Real'] = ano_atual - df['Ano_Nascimento']

erros_idade = df[df['Idade_Declarada'] != df['Idade_Real']].copy()

print(f"--- Relatório de Inconsistências (Ano Base: {ano_atual}) ---")
if erros_idade.empty:
    print("Nenhuma contradição encontrada.")
else:
    print(erros_idade[['Nome', 'Ano_Nascimento', 'Idade_Declarada', 'Idade_Real']])