def main():
    aberto = triado = encaminhado = False
    while True:
        uEntry = input("""\nVocê está simulando um atendimento. Comandos:
        A -> Abrir atendimento
        T -> Triagem
        E -> Encaminhar
        F -> Finalizar
        S -> Sair
        Insira o comando: """).upper()
    
        match uEntry:
            case "A":
                if aberto:
                    print("\nO atendimento já está aberto.")
                else:
                    print("\nAtendimento aberto.")
                    aberto =  True 
            case "T":
                if not aberto:
                    print("\nErro: Abra o atendimento antes de começar a triagem (comando A).")        
                elif triado:
                    print("\nA triagem já está em andamento.")
                else:
                    print("\nTriagem em andamento...")
                    triado = True
            case "E":
                if not aberto:
                    print("\nErro: Abra o atendimento primeiro (comando A).")
                elif not triado:
                    print("\nErro: Realize a triagem antes de encaminhar (comando T).")
                elif encaminhado:
                    print("\nPaciente já encaminhado.")
                else:
                    print("\nPaciente encaminhado com sucesso!")
                    encaminhado = True
            case "F":
                if not aberto:
                    print("\nErro: Abra o atendimento primeiro (comando A).")
                elif not triado:
                    print("\nErro: Realize a triagem antes de finalizar (comando T).")
                elif not encaminhado:
                    print("\nErro: Encaminhe o paciente antes de finalizar (comando E).")
                else:
                    print("\nAtendimento finalizado com sucesso!")
                    aberto = triado = encaminhado = False
            case "S":
                print("\nServiço de atendimento: Off")
                break
            case _:
                print(f"\nComando {uEntry} inválido! Use A, T, E, F ou S.")

if __name__ == "__main__":
    main()