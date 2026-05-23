import datetime
from .contato import Contato

class Evento:
    __slots__ = ('_descricao', '_data_inicio', '_data_fim', '_contato')
    _total_eventos: int = 0
    
    def __init__(self, descricao: str, data_inicio: datetime.date, data_fim: datetime.date, contato: Contato):
        self._descricao: str = descricao
        self._data_inicio: datetime.date = data_inicio
        self._data_fim: datetime.date = data_fim
        self._contato: Contato = contato
        Evento._total_eventos += 1
        
    def get_informacoes(self) -> str:
        return( f"Evento: {self._descricao}\nInício: {self._data_inicio}\nFim: {self._data_fim}\nContato: {self._contato.nome}")
    
    @staticmethod
    def get_total_eventos() -> int:
        return Evento._total_eventos