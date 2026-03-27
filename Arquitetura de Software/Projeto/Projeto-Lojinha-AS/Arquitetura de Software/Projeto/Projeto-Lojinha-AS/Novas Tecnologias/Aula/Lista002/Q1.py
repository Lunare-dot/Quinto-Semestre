import string
import unicodedata

def uText(text: str) -> str:
    normalize = unicodedata.normalize("NFD", text)
    noAcc = "".join(c for c in normalize if unicodedata.category(c) != "Mn")

    punctuation = string.punctuation + " "
    translator = str.maketrans("", "", punctuation)
    testSubject = noAcc.translate(translator).lower()
    return testSubject

def main():
    uEntry = input("Digite uma frase ou palavra: ")
    entrySubject = uText(uEntry)

    status = "Palíndromo!" if entrySubject == entrySubject[::-1] else "Não é palíndromo!"
    print(f"{uEntry} -> {status}")

if __name__ == "__main__":
    main()