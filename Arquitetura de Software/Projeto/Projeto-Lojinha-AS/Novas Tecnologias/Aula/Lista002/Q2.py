import math

def main():
    hourEntry = int(input("Horas: "))
    rainEntry = int(input("Está chovendo?\n(1 - Sim, 2 - Não): "))
    fluxEntry = int(input("Fluxo do trânsito\n(0 - Baixo, 1 - Intermediário, 2 - Alto): "))
    time = 0

    if hourEntry < 0 or hourEntry > 23:
        print("Hora: entrada inválida.")
        return
    
    if rainEntry not in (0, 1):
        print("Chuva: Entrada inválida.")
        return

    if fluxEntry not in (0, 1, 2):
        print("Fluxo: Entrada inválida.")
        return
    
    if hourEntry in range(7, 9) or hourEntry in range(17, 19):
        time = 60
    else:
        time = 35

    if rainEntry == 1:
        time += time * 0.2

    if fluxEntry == 2:
        time += 15
    elif fluxEntry == 0:
        time -= 10

    print(math.ceil(time))

if __name__ == "__main__":
    main()