from entity.evento import Evento
from entity.agenda import Agenda
from entity.contato import Contato

class EventoService:
    
    @staticmethod
    def criar():
        desc = input("\nDescrição do evento: ")
        data_inicio = input("Início do evento (data): ")
        data_fim = input("Fim do evento (data): ")
        nome_contato = input("Nome do contato: ")
        
        for contato in Agenda.contatos():
            if contato.nome == nome_contato:
                evento = Evento(desc, data_inicio, data_fim, contato)
                Agenda(evento)
                print("Evento criado com sucesso!")
                return
            
        print("\nContato não encontrado. Associe um contato existente.\n")
        return

    def listar():
        if not Agenda.eventos():
            print("\nNenhum evento registrado!")
            return
        
        for evento in Agenda.eventos():
            print(f"\n{evento.get_informacoes()}\n")
            
    def total_eventos():
        return Evento.get_total_eventos()