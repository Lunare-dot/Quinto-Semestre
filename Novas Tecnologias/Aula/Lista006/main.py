from services import ContatoService

def main():
    while True:
        user_entry = input(f"\nEscolha uma opção (1 ~ 4): \n"
        f"1 - Criar, editar e listar contatos\n"
        f"2 - Criar contatos de emergência\n"
        f"3 - Criar e listar eventos\n"
        f"4 - Sair\n")
        
        if not user_entry.isdigit():
            print("Digite apenas números.")
            continue
        
        num = int(user_entry)
        if num > 4 or num < 1:
            print("Escolha uma opção de 1 a 4: ")
            continue
        
        match num:
            case 1:
                opt_entry = input(f"\nSelecione a opção (1 ~ 4): \n"
                f"1 - Criar\n"
                f"2 - Editar\n"
                f"3 - Listar\n"
                f"4 - Voltar\n")
                
                if not opt_entry.isdigit():
                    print("Digite apenas números.")
                    continue
                
                opt1 = int(opt_entry)
                if opt1 > 4 or opt1 < 1:
                    print("\nEscolha uma opção de 1 a 4: ")
                    continue
                
                match opt1:
                    case 1:
                        ContatoService.criar()
                        continue
                    case 2:
                        ContatoService.editar()
                        continue
                    case 3:
                        ContatoService.listar()
                        continue
                    case 4:
                        return           
                
            case 2:
                continue
                
            case 3:
                continue
                
            case 4:
                break
                
            case _:
                continue
    
if __name__ == "__main__":
    main()