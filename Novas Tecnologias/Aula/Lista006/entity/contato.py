import datetime

class Contato:
    __slots__ = ('_nome', '_telefone', '_datanasc', '_email')
    def __init__(self, nome: str, telefone: str, datanasc: datetime.date, email: str):
        self.nome: str = nome
        self.telefone: str = telefone
        self.datanasc: datetime.date = datanasc
        self.email: str = email
        
    @staticmethod
    def _converter_data(data) -> datetime.date:
        if isinstance(data, datetime.date):
            return data
        elif isinstance(data, str):
            return datetime.datetime.strptime(data, "%d/%m/%Y").date()
        else:
            raise TypeError("A data de nascimento deve ser string ou datetime.date (d/m/a)")
        
    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def telefone(self) -> str:
        return self._telefone
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
        
    @property
    def datanasc(self) -> datetime.date :
        return self._datanasc
    @datanasc.setter
    def datanasc(self, datanasc):
        self._datanasc = Contato._converter_data(datanasc)
        
    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
        
    def __str__(self):
        return (f"{self.nome}\n{self.telefone}\n{self.datanasc:%d/%m/%Y}\n{self.email}")