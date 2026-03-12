def vowelCount(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence.lower() if char in vowels)

sentence = input("Insira uma frase: ")
contador = vowelCount(sentence)
print(f"Existem {contador} vogais nessa frase.")