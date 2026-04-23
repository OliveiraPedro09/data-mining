# 1 - Verificar se no conjunto existe algum outlier (< -5 ou > 75)
import statistics
tempos = [20, 25, 30, 35, 40, 45, 90]
q2 = statistics.median(tempos)

inferior = tempos[:3]
superior = tempos[4:]

q1 = statistics.median(inferior)
q3 = statistics.median(superior)

iqr = q3 - q1

limite_inferior = q1 - (1.5 * iqr)
limite_superior = q3 + (1.5 * iqr)
outliers = []

for tempo in tempos:
    if tempo < limite_inferior or tempo > limite_superior:
        outliers.append(tempo)

print(f"Outliers encontrados: {outliers}")

# 2 - Alterar a verificação do conjunto para tornar genérico (para qualquer tamanho)
tempos.sort()

n = len(tempos)
meio = n // 2
q2 = statistics.median(tempos)
    
inferior = tempos[:meio]
superior = tempos[meio + 1:] if n % 2 != 0 else tempos[meio:]

q1 = statistics.median(inferior)
q3 = statistics.median(superior)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = [t for t in tempos if t < limite_inferior or t > limite_superior]

print(f"Resultados para N={n}:")
print(f"Q1: {q1} | Q2: {q2} | Q3: {q3}")
print(f"Limites: {limite_inferior} até {limite_superior}")
print(f"Outliers detectados: {outliers}")