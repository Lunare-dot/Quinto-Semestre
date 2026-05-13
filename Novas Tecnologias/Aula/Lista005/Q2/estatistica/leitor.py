import csv

def converter(valor):
    try:
        return int(valor)
    except:
        try:
            return float(valor)
        except:
            return valor

def ler_csv(caminho):
    dados = []

    with open(caminho, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        
        for linha in leitor:
            
            linhaConvert = {}
            
            for chave, valor in linha.items():
                linhaConvert[chave] = converter(valor)
                
            dados.append(linhaConvert)
            
    return dados