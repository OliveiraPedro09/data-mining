# =========================================
# EXERCÍCIOS DE MINERAÇÃO DE DADOS
# Z-Score, Isolation Forest e Normalização
# =========================================

# --------------------------
# EXERCÍCIO 1
# --------------------------
# Um sensor de temperatura ESP32 envia leituras.
# Precisamos imprimir apenas as temperaturas com Z-Score > 2.5.

from scipy.stats import zscore
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler

temp = [45.5, 46.0, 45.2, 45.8, 46.1, 98.0, 45.9, 45.3]

z_temp = zscore(temp)

print("Exercício 1")
print("Temperaturas anômalas:")
for valor, z in zip(temp, z_temp):
    if z > 2.5:
        print(f"Temperatura: {valor} | Z-Score: {z:.2f}")
print("-" * 50)


# --------------------------
# EXERCÍCIO 2
# --------------------------
# Monitoramento de voltagem.
# Disparar alerta se algum Z-Score for menor que -2.0.

voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]
z_voltagem = zscore(voltagem)

print("Exercício 2")
print("Z-Scores da voltagem:", np.round(z_voltagem, 2))

if any(z < -2.0 for z in z_voltagem):
    print("Falha de Energia!")
print("-" * 50)


# --------------------------
# EXERCÍCIO 3
# --------------------------
# Criar DataFrame, adicionar coluna z_score
# e filtrar dados com Z-Score absoluto entre -3 e 3.

vendas = [1200, 1350, 1250, 1300, 13500, 1280]

df_vendas = pd.DataFrame({"vendas": vendas})
df_vendas["z_score"] = zscore(df_vendas["vendas"])

dados_limpos = df_vendas[df_vendas["z_score"].abs() <= 3]

print("Exercício 3")
print("DataFrame original:")
print(df_vendas)
print("\nDataFrame filtrado:")
print(dados_limpos)
print("-" * 50)


# --------------------------
# EXERCÍCIO 4
# --------------------------
# Mostrar como um outlier colossal pode inflar média e desvio padrão.

medidas = [10, 12, 11, 10, 10000]
z_medidas = zscore(medidas)

media_medidas = np.mean(medidas)
desvio_medidas = np.std(medidas)

print("Exercício 4")
print("Lista:", medidas)
print("Média:", media_medidas)
print("Desvio padrão:", desvio_medidas)
print("Z-Score do valor 10000:", z_medidas[-1])

if z_medidas[-1] > 3:
    print("O valor 10000 ultrapassa a marca de 3.")
else:
    print("O valor 10000 NÃO ultrapassa a marca de 3.")
print("-" * 50)


# --------------------------
# EXERCÍCIO 5
# --------------------------
# Isolation Forest em dados multivariados de servidores.

servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

modelo_serv = IsolationForest(random_state=42, contamination=0.2)
modelo_serv.fit(servidores)
pred_serv = modelo_serv.predict(servidores)

print("Exercício 5")
print("Predições:", pred_serv)
print("Obs.: no Isolation Forest, -1 significa anomalia e 1 significa dado normal.")
print("-" * 50)


# --------------------------
# EXERCÍCIO 6
# --------------------------
# Comparar contamination=0.05 e contamination=0.20

np.random.seed(42)

# 1000 linhas normais
dados_normais = np.random.normal(loc=50, scale=5, size=(1000, 2))

# 50 linhas absurdas
anomalias = np.random.normal(loc=200, scale=20, size=(50, 2))

dataset = np.vstack([dados_normais, anomalias])

modelo_005 = IsolationForest(contamination=0.05, random_state=42)
pred_005 = modelo_005.fit_predict(dataset)

modelo_020 = IsolationForest(contamination=0.20, random_state=42)
pred_020 = modelo_020.fit_predict(dataset)

qtd_anomalias_005 = np.sum(pred_005 == -1)
qtd_anomalias_020 = np.sum(pred_020 == -1)

print("Exercício 6")
print("Anomalias detectadas com contamination=0.05:", qtd_anomalias_005)
print("Anomalias detectadas com contamination=0.20:", qtd_anomalias_020)
print("-" * 50)


# --------------------------
# EXERCÍCIO 7
# --------------------------
# Detectar o aluno [9, 25] como anomalia usando duas dimensões.

alunos = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

modelo_alunos = IsolationForest(contamination=0.34, random_state=42)
pred_alunos = modelo_alunos.fit_predict(alunos)

print("Exercício 7")
for aluno, pred in zip(alunos, pred_alunos):
    print(f"Aluno {aluno} -> {pred}")
print("Obs.: o aluno [9, 25] tende a ser tratado como anomalia porque a combinação nota alta + faltas altas foge do padrão.")
print("-" * 50)


# --------------------------
# EXERCÍCIO 8
# --------------------------
# Criar DataFrame com uma linha absurda e marcar outlier.

df_alunos = pd.DataFrame({
    "idade": [18, 19, 20, 21, 22, 150],
    "horas_estudo": [10, 12, 9, 11, 13, 2],
    "nota_final": [7.5, 8.0, 7.8, 8.2, 8.5, 3.0]
})

modelo_df = IsolationForest(contamination=0.17, random_state=42)
df_alunos["Outlier"] = modelo_df.fit_predict(df_alunos)

anomalias_df = df_alunos[df_alunos["Outlier"] == -1]

print("Exercício 8")
print("DataFrame completo:")
print(df_alunos)
print("\nLinha(s) anômala(s):")
print(anomalias_df)
print("-" * 50)


# --------------------------
# EXERCÍCIO 9
# --------------------------
# Min-Max manual e com scaler.

# Fórmula:
# x_norm = (x - min) / (max - min)

x = 200
minimo = 100
maximo = 500

normalizado_manual = (x - minimo) / (maximo - minimo)

pressao = [[100], [200], [500]]
scaler_pressao = MinMaxScaler()
pressao_normalizada = scaler_pressao.fit_transform(pressao)

print("Exercício 9")
print("Valor normalizado manual de 200 psi:", normalizado_manual)
print("Valores com MinMaxScaler:")
print(pressao_normalizada)
print("-" * 50)


# --------------------------
# EXERCÍCIO 10
# --------------------------
# Mostrar como a normalização reduz o impacto da escala do saldo.

df_clientes = pd.DataFrame({
    "Saldo": [1000000, 1000010],
    "Risco": [0.1, 0.9]
}, index=["Cliente A", "Cliente B"])

scaler_clientes = MinMaxScaler()
df_clientes_norm = pd.DataFrame(
    scaler_clientes.fit_transform(df_clientes),
    columns=df_clientes.columns,
    index=df_clientes.index
)

print("Exercício 10")
print("Sem normalização:")
print(df_clientes)
print("\nCom normalização:")
print(df_clientes_norm)
print("-" * 50)


# --------------------------
# EXERCÍCIO 11
# --------------------------
# Aplicar MinMaxScaler em temperaturas negativas.

temps = [[-20], [-10], [0], [20]]

scaler_temps = MinMaxScaler()
temps_normalizadas = scaler_temps.fit_transform(temps)

print("Exercício 11")
print("Temperaturas normalizadas:")
print(temps_normalizadas)
print("-" * 50)


# --------------------------
# EXERCÍCIO 12
# --------------------------
# Remover outlier de produção com Z-Score e depois normalizar.
# Observação importante: com esse conjunto pequeno, o Z-Score clássico
# pode não passar de 3 para o valor 500. Então aqui usamos um critério
# mais prático: remover o valor com maior |Z| quando ele claramente destoa.

producao = [100, 102, 98, 105, 500, 101]
z_producao = zscore(producao)

# Identifica o índice do maior |z|
indice_outlier = np.argmax(np.abs(z_producao))
valor_outlier = producao[indice_outlier]

# Remove esse valor
producao_limpa = [v for i, v in enumerate(producao) if i != indice_outlier]

# Normaliza os dados limpos
scaler_producao = MinMaxScaler()
producao_normalizada = scaler_producao.fit_transform(np.array(producao_limpa).reshape(-1, 1))

print("Exercício 12")
print("Z-Scores:", np.round(z_producao, 2))
print("Outlier removido:", valor_outlier)
print("Produção limpa:", producao_limpa)
print("Produção normalizada:")
print(producao_normalizada.flatten().tolist())
print("-" * 50)