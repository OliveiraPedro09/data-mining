dados = [100, 150, 200, 250, 300, 350]

# ponto médio
tamanho = len(dados)
meio = tamanho // 2

metade_inferior = dados[:meio]
metade_superior = dados[meio:]

# Calcular a mediana de cada metade
def calcular_mediana_simples(lista):
    n = len(lista)
    m = n // 2
    if n % 2 != 0:
        return lista[m]
    else:
        return (lista[m-1] + lista[m]) / 2

q1 = calcular_mediana_simples(metade_inferior)
q3 = calcular_mediana_simples(metade_superior)

print(f"Metade Inferior: {metade_inferior} -> Q1: {q1}")
print(f"Metade Superior: {metade_superior} -> Q3: {q3}")