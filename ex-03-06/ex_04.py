import pandas as pd

dados = {
    'Sistema_Operacional': (
        ['Ubuntu'] * 5000 +
        ['Debian'] * 3000 +
        ['Armbian'] * 1500 +
        ['Ubuntuu'] * 150 +
        ['Debian10'] * 100 +
        ['Armmbiian'] * 50
    )
}

df = pd.DataFrame(dados)

proporcoes = df['Sistema_Operacional'].value_counts(normalize=True)

categorias_raras = proporcoes[proporcoes < 0.05].index

df_erros = df[df['Sistema_Operacional'].isin(categorias_raras)]

print("--- Categorias identificadas como raras (< 5%) ---")
print(proporcoes[proporcoes < 0.05])

print(f"\nTotal de linhas com possíveis erros: {len(df_erros)}")