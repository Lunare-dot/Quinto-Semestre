from .contato import Contato
from datetime import datetime

class ContatoEmergencia(Contato):
    __slots__ = ('_prioridade',)
    def __init__(self, nome: str, telefone: str, datanasc: datetime, email: str, prioridade: bool = True):
        super().__init__(nome, telefone, datanasc, email)
        self._prioridade: bool = prioridade
        
    @property
    def prioridade(self) -> bool:
        return self._prioridade