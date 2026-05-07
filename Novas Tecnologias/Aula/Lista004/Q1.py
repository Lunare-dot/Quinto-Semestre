palavras = ['casa','corinthians','amanha']
lista = []

for palavra in palavras:
    dict = {}
    for letra in palavra:
        dict[letra] = dict.get(letra, 0) + 1
    lista.append(dict)

print(lista)