from .contato import Contato
from .evento import Evento

class Agenda:
    __contatos = []
    __eventos = []
    
    def __init__(self, item = None):
        if item is not None:
            if isinstance(item, Contato):
                self.__contatos.append(item)
            elif isinstance(item, Evento):
                self.__eventos.append(item)
                
    @staticmethod
    def contatos() -> list[Contato]:
        return Agenda.__contatos
    
    @staticmethod
    def eventos() -> list[Evento]:
        return Agenda.__eventos