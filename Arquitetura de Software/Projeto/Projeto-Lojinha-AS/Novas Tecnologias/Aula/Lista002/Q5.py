def main():
    iEntry = int(input("Digite o valor inicial (a): "))
    fEntry = int(input("Digite o valor final (b): "))
    pEntry = int(input("Digite o passo: "))
    
    if pEntry == 0:
        print("Erro: o passo não pode ser zero.")
        return
    
    if iEntry < fEntry and pEntry < 0:
        print("Erro: passo deve ser positivo quando a < b.")
        return
    
    if iEntry > fEntry and pEntry > 0:
        print("Erro: passo deve ser negativo quando a > b.")
        return
    
    count = 0
    for i in range(iEntry, fEntry + pEntry, pEntry):
        if(pEntry > 0 and i <= fEntry) or (pEntry < 0 and i >= fEntry):
            print(i)
            count += 1
            
    print(f"Total de valores impressos: {count}")
    
    
if __name__ == "__main__":
    main()