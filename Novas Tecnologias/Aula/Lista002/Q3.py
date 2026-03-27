def isAnagram(text1, text2):
    subject1 = text1.replace(" ", "").lower()
    subject2 = text2.replace(" ", "").lower()

    return sorted(subject1) == sorted(subject2)

def main():
    uEntry1 = input("Digite a primeira palavra: ")
    uEntry2 = input("Digite a segunda palavra: ")

    if isAnagram(uEntry1, uEntry2):
        print(f"{uEntry1} e {uEntry2} são anagramas!")
    else:
        print(f"{uEntry1} e {uEntry2} não são anagramas!")

if __name__ == "__main__":
    main()