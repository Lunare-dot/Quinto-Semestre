from entity.contato import Contato
from entity.agenda import Agenda
from entity.contatoemergencia import ContatoEmergencia

class ContatoService:

    @staticmethod
    def criar():
        nome = input("\nNome do contato: ")
        telefone = input("Telefone do contato: ")
        datanasc = input("Data de nascimento do contato: ")
        email = input("Email do contato: ")
        
        contact = Contato(nome, telefone, datanasc, email)
        Agenda(contact)
        
        print("Contato criado!")
        
    @staticmethod
    def listar():
        contatos = Agenda.contatos()
        
        if not contatos:
            print("\nNenhum contato cadastrado!\n")
            return
        
        for c in contatos:
            if isinstance(c, ContatoEmergencia):
                print(f"\n[EMERGÊNCIA]:\n{c}")
            else:
                print(f"\n{c}")
            
    @staticmethod
    def editar():
        contatos = Agenda.contatos()
        
        if not contatos:
            print("\nNenhum contato cadastrado!\n")
            return
        
        for i, contato in enumerate(contatos):
            print(f"\n{i} - {contato}")
        
        index = int(input(f"\nSelecione o contato a ser editado: \n"))
        contato = contatos[index]
        
        novo_nome = input("Nome: ")
        contato.nome = novo_nome
        
        novo_telefone = input("Telefone: ")
        contato.telefone = novo_telefone
        
        nova_datanasc = input("Data de nascimento: ")
        contato.datanasc = nova_datanasc
        
        novo_email = input("Email: ")
        contato.email = novo_email
        
        print("Contato atualizado!")