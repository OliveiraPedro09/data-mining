import pandas as pd

# =========================
# TABELA CLIENTES
# =========================
df_clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nome_cliente': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'estado': ['SP', 'RJ', 'MG', 'SP', 'BA']
})

# =========================
# TABELA PRODUTOS
# =========================
df_produtos = pd.DataFrame({
    'id_produto': [101, 102, 103, 104],
    'nome_produto': ['Notebook', 'Placa de Vídeo', 'SSD', 'Memória RAM'],
    'categoria': ['Hardware', 'Hardware', 'Hardware', 'Hardware']
})

# =========================
# TABELA VENDAS
# =========================
df_vendas = pd.DataFrame({
    'id_venda': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'id_cliente': [1, 2, 3, 1, 4, 5, 2, 3],
    'id_produto': [101, 102, 103, 101, 104, 102, 101, 104],
    'quantidade': [1, 2, 1, 1, 3, 1, 2, 1]
})

print(df_clientes)
print(df_produtos)
print(df_vendas)
