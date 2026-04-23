import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    'Nome_Completo': ['Ana', 'Beto', 'Carla', None, 'Edu'],
    'Email': ['ana@ex.com', None, 'carla@ex.com', None, 'edu@ex.com'],
    'Telefone': [None, None, '9999-0000', None, '8888-1111'],
    'Idade': [25, 30, None, None, 40],
    'Cargo': ['Engenheira', 'Analista', None, None, 'Gerente']
}

df = pd.DataFrame(dados)

plt.figure(figsize=(10, 6))

sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

plt.title('Mapa de Qualidade de Dados: Áreas em Amarelo representam Dados Faltantes')
plt.show()