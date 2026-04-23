import pandas as pd
import random

# Motoristas
motoristas = [
    "Carlos Silva",
    "Ana Souza",
    "Marcos Lima",
    "Fernanda Alves",
    "João Pereira"
]

# Veículos
veiculos = [
    {"veiculo_id": 1, "tipo": "Caminhão"},
    {"veiculo_id": 2, "tipo": "Van"},
    {"veiculo_id": 3, "tipo": "Moto"},
    {"veiculo_id": 4, "tipo": "Caminhão"},
    {"veiculo_id": 5, "tipo": "Van"}
]

# Gerar entregas
entregas = []

for i in range(1, 101):
    motorista = random.choice(motoristas)
    veiculo = random.choice(veiculos)

    entrega = {
        "Entrega_ID": i,
        "Motorista": motorista,
        "Veiculo_ID": veiculo["veiculo_id"],
        "Tipo_Veiculo": veiculo["tipo"],
        "Distancia_Km": random.randint(5, 300),
        "Status_Entrega": random.choice(["Entregue", "Atrasada", "Cancelada"])
    }

    entregas.append(entrega)

df = pd.DataFrame(entregas)

# Salvar arquivo
df.to_csv("logistica_frota.csv", index=False)

print("Arquivo gerado com sucesso!")
