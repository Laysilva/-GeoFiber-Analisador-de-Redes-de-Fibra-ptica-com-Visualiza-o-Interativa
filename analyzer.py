def calcular_kpis(df):
    total_incidentes = len(df)
    resolvidos = df[df['status'] == 'resolvido']
    pendentes = df[df['status'] == 'pendente']
    tempo_medio_reparo = resolvidos['tempo_reparo'].mean()
    return {
        'total': total_incidentes,
        'resolvidos': len(resolvidos),
        'pendentes': len(pendentes),
        'tempo_medio_reparo': tempo_medio_reparo
    }