from services import ContatoService
from services import EmergenciaService
from services import EventoService

def main():
    
    while True:
        user_entry = input(f"\nEscolha uma opção (1 ~ 4): \n"
        f"1 - Criar, editar e listar contatos\n"
        f"2 - Criar contatos de emergência\n"
        f"3 - Criar e listar eventos\n"
        f"4 - Sair\n")
        
        if not user_entry.isdigit():
            print("\nDigite apenas números.\n")
            continue
        
        num = int(user_entry)
        if num > 4 or num < 1:
            print("\nSomente números inteiros de 1 a 4.\n")
            continue
        
        match num:
            case 1:
                opt_entry = input(f"\nEscolha uma opção (1 ~ 4): \n"
                f"1 - Criar\n"
                f"2 - Editar\n"
                f"3 - Listar\n"
                f"4 - Voltar\n")
                
                if not opt_entry.isdigit():
                    print("\nDigite apenas números.\n")
                    continue
                
                opt1 = int(opt_entry)
                if opt1 > 4 or opt1 < 1:
                    print("\nSomente números inteiros de 1 a 4.\n")
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
                        continue          
                
            case 2:
                EmergenciaService.criar()
                continue
                
            case 3:
                opt_entry = input(f"\nEscolha uma opção (1 ~ 2):\n"
                f"1 - Criar evento\n"
                f"2 - Listar eventos\n"
                f"3 - Voltar\n")
                
                if not opt_entry.isdigit():
                    print("\nDigite apenas números.\n")
                    continue
                
                opt3 = int(opt_entry)
                if opt3 > 3 or opt3 < 1:
                    print("\nSomente números inteiros de 1 a 3.\n")
                    continue
                
                match opt3:
                    case 1:
                        EventoService.criar()
                        continue
                    case 2:
                        EventoService.listar()
                        continue
                    case 3:
                        continue
                
            case 4:
                print(f"Quantidade total de eventos: {EventoService.total_eventos()}")
                break
    
if __name__ == "__main__":
    main()