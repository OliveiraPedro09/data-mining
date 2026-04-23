import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

# -----------------------------
# TABELA USUARIOS
# -----------------------------
usuarios = []
departamentos = ["Financeiro", "RH", "TI", "Marketing", "Vendas", "Operações"]

for i in range(1, 51):
    usuarios.append({
        "id_usuario": i,
        "nome_usuario": fake.name(),
        "departamento": random.choice(departamentos)
    })

df_usuarios = pd.DataFrame(usuarios)


# -----------------------------
# TABELA EQUIPAMENTOS
# -----------------------------
sistemas = ["Windows 10", "Windows 11", "Ubuntu", "macOS"]

equipamentos = []

for i in range(1, 51):
    equipamentos.append({
        "id_equipamento": i,
        "id_usuario": random.randint(1, 50),
        "sistema_operacional": random.choice(sistemas),
        "modelo": random.choice(["Dell", "Lenovo", "HP", "Apple"])
    })

df_equipamentos = pd.DataFrame(equipamentos)


# -----------------------------
# TABELA CHAMADOS
# -----------------------------
chamados = []

for i in range(1, 301):
    chamados.append({
        "id_ticket": i,
        "id_usuario": random.randint(1, 50),
        "id_equipamento": random.randint(1, 50),
        "categoria": random.choice(["Hardware", "Software", "Rede", "Acesso"]),
        "horas_resolucao": round(random.uniform(0.5, 8), 2)
    })

df_chamados = pd.DataFrame(chamados)


# -----------------------------
# SALVAR CSV
# -----------------------------
df_usuarios.to_csv("usuarios.csv", index=False)
df_equipamentos.to_csv("equipamentos.csv", index=False)
df_chamados.to_csv("chamados.csv", index=False)

print("Arquivos gerados com sucesso!")
