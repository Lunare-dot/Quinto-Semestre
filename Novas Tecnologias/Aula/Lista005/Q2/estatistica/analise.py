def estatisticas(dados, campo):
    valores = []
    
    for item in dados:
        valores.append(item[campo])
        
    resultado = {
        "media": sum(valores)/len(valores),
        "mínimo": min(valores),
        "máximo": max(valores),
        "total": sum(valores)
    }
    
    return resultado