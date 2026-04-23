import pandas as pd

def fatiar_turnos_log(lista_horarios):
    df = pd.DataFrame(lista_horarios, columns=['hora'])
    limites = [0, 6, 18, 24]
    nomes_turnos = ['Madrugada', 'Comercial', 'Noite']

    df['turno'] = pd.cut(df['hora'], bins=limites, labels=nomes_turnos, right=False)
    
    return df

horarios_log = [2, 7, 10, 15, 19, 23]

df_resultado = fatiar_turnos_log(horarios_log)
print(df_resultado)