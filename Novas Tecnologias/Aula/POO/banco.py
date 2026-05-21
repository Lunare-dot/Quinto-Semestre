class Conta:
    __slots__=['__numero', 'titular', 'saldo', 'limite']
    _total_contas = 0

    #método reservado, vai inicializar o objeto da classe Conta
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.__numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        Conta._total_contas += 1
            
	# o método __new__() é realmente o construtor
	# o método __init__() é o responsável por inicializar o objeto
	# self é a referencia do objeto

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
	
    def deposita(self, valor):
        self.saldo+=valor
        
    def saca(self, valor):
        if(self.saldo<valor):
            return False
        else:
            self.saldo -= valor
            return True
		
    def extrato(self):
            print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True
        
    def __str__(self):
        print(self.__numero, self.titular, self.saldo, self.limite)

#    @staticmethod
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

class Cliente:
    __slots__ = ['nome', 'sobrenome', 'cpf']

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf