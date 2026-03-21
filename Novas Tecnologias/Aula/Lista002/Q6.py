def main():
    loop = 5
    aOpen = tBool = eBool = False
    while loop > 1:
        uEntry = input("""\nVocê está simulando um atendimento. Comandos:
        A -> Abrir atendimento
        T -> Triagem
        E -> Encaminhar
        F -> Finalizar
        S -> Sair
        Insira o comando: """).upper()
    
        match uEntry:
            case "A":
                print("\nAtendimento aberto.")
                aOpen =  True
                loop -= 1
            case "T":
                if aOpen:
                    print("\nTriagem em andamento...")
                    tBool = True
                    loop -= 1
                else:
                    print("\nRequisitos não atendidos. Execute etapas anteriores antes da triagem.")
            case "E":
                if tBool and aOpen:
                    print("\nVocê será encaminhado para...")
                    eBool = True
                    loop -= 1
                else:
                    print("\nRequisitos não atendidos. Execute etapas anteriores antes de encaminhar.")
            case "F":
                if eBool and tBool and aOpen:
                    print("\nAtendimento finalizado!")
                    loop -= 1
                else:
                    print("\nRequisitos não atendidos. Execute etapas anteriores antes de finalizar")
            case "S":
                print("Serviço de atendimento: Off")
                loop = 0
            case _:
                print("Comando inválido!")

if __name__ == "__main__":
    main()