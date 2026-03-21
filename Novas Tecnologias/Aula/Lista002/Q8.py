def entryClass(n: int) -> tuple[int, list[int], str]:
    divisores = [i for i in range(1, n) if n % i == 0]
    soma = sum(divisores)
    
    if soma ==  n:
        classe = "perfeito"
    elif soma > n:
        classe = "abundante"
    else:
        classe = "deficiente"

    return classe, soma, divisores 

def tryPos() -> int:
    while True:
        try:
            n = int(input("Digite um número inteiro e positivo: "))
            if n > 0:
                return n
            print("Error: o número deve ser maior que zero.")
        except ValueError:
            print("Error: o número deve ser positivo.")
    
    
def main():
    n = tryPos()
    classe, soma, divisores = entryClass(n)
    
    print(f"\nDivisores próprios: {divisores}")
    print(f"Soma dos divisores: {soma}")
    print(f"Classificação do número: {classe}")

if __name__ == "__main__":
    main()