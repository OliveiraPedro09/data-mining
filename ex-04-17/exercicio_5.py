def calcular_metricas_sensor(leitura_t1, leitura_t2):
    delta = leitura_t2 - leitura_t1
    
    evolucao_pct = (delta / leitura_t1) * 100
    
    tendencia = 1 if delta > 0 else 0
    
    print(f"Leitura Inicial: {leitura_t1} | Leitura Atual: {leitura_t2}")
    print(f"Delta: {delta} | Evolução: {evolucao_pct:.2f}% | Crescimento: {bool(tendencia)}")

calcular_metricas_sensor(150, 185)