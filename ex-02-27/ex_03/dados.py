import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ==============================
# TABELA DE AMBIENTES
# ==============================

df_ambientes = pd.DataFrame({
    "id_ambiente": [1, 2, 3, 4],
    "nome_setor": [
        "Produção",
        "Armazém",
        "Laboratório",
        "Área Externa"
    ]
})

# ==============================
# TABELA DE DISPOSITIVOS
# ==============================

df_dispositivos = pd.DataFrame({
    "id_dispositivo": [101,102,103,104,105,106],
    "tipo_dispositivo": [
        "Raspberry Pi",
        "ESP32",
        "Orange Pi",
        "ESP32",
        "Raspberry Pi",
        "ESP32"
    ],
    "id_ambiente": [1,1,2,3,4,2]
})

# ==============================
# GERAR TELEMETRIA
# ==============================

registros = []

inicio = datetime(2025,1,1,0,0)

for i in range(200):

    data_hora = inicio + timedelta(minutes=i*10)

    for dispositivo in df_dispositivos["id_dispositivo"]:

        temperatura = np.random.normal(25, 3)
        umidade = np.random.normal(60, 10)

        registros.append({
            "id_dispositivo": dispositivo,
            "data_hora": data_hora,
            "temperatura_c": round(temperatura,2),
            "umidade_pct": round(umidade,2)
        })

df_telemetria = pd.DataFrame(registros)

# ==============================
# SALVAR CSV PARA POWER BI
# ==============================

df_ambientes.to_csv("ambientes.csv", index=False)
df_dispositivos.to_csv("dispositivos.csv", index=False)
df_telemetria.to_csv("telemetria.csv", index=False)

print("Arquivos CSV gerados com sucesso!")
