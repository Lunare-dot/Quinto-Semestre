def main():
    words = ["uva", "maçã", "pêra", "abacaxi"]

    term = input("Digite o termo a ser buscado: ")
    found = False

    for i in range(len(words)):
        if words[i].lower() == term.lower():
            return print(f"Termo encontrado no índice {i + 1}!")
            found = True
            break

    if not found:
        print("Termo não encontrado!") 

if __name__ == "__main__":
    main()