def factCalc(n):
    limiter = 1_000_000
    result = 1
    checkLimit = False
    if n < 0:
        print("Erro!")
    else:
        for k in range(2, n + 1):
            result *= k
            if result > limiter:
                print(f"Resultado estourou o limite em {k}")
                print(f"Valor acumulado: {result}")
                checkLimit = True
                break
        if not checkLimit:
            print(f"O resultado de {n}! é: {result}")

def main():
    uEntry = int(input("Digite um número inteiro: "))
    factCalc(uEntry)

if __name__ == "__main__":
    main()