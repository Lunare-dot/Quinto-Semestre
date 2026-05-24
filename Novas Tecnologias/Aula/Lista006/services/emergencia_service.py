from entity.contatoemergencia import ContatoEmergencia
from entity.agenda import Agenda

class EmergenciaService:
    
    @staticmethod
    def criar():
        nome = input("\nNome do contato de emergência: ")
        telefone = input("Telefone do contato de emergência: ")
        datanasc = input("Data de nascimento do contato de emergência: ")
        email = input("Email do contato de emergência: ")
        
        contato_emergencia = ContatoEmergencia(nome, telefone, datanasc, email)
        
        Agenda(contato_emergencia)
        print("Contato de emergência criado com sucesso!")