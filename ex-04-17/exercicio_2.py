import pandas as pd

def extrair_features_tempo(timestamps):
    df = pd.DataFrame({'data': pd.to_datetime(timestamps)})
    df['mes'] = df['data'].dt.month
    df['dia_semana'] = df['data'].dt.day_name()
    df['is_final_semana'] = (df['data'].dt.weekday >= 5).astype(int)
    return df

tempos = ["2026-04-17", "2026-04-18", "2026-04-19"]
print(extrair_features_tempo(tempos))