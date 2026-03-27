def cesarCypher(text, shift):
    r = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            char = chr((ord(char) - start + shift) % 26 + start)
        r += char
    return r
    
text = input("Mensagem a ser criptografada: ")
shift = int(input("Deslocamento: "))
cypher = cesarCypher(text, shift)
print(cypher)