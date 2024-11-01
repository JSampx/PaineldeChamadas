class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ChamaSenha(metaclass=SingletonMeta):
    contador: int = 0
    lista: list = []


    def __init__(self):
        pass

    def incluiLista(self, Senha):
        if Senha.__repr__() in self.lista:
            print(f'A senha {Senha.__repr__()} já existe na lista')
            self.lista.append(f'{str(Senha)[0]}{Senha.seq + 1}')
            self.contador += 1
        else:
            self.lista.append(Senha.__repr__())
            self.contador += 1
        print(self.lista)

tipos = []
class Senha:
    tipo: str
    seq: int = 0
    def __init__(self, tipo: str):
        senha = TipoSenha(tipo)
        self.tipo = senha
        self.seq += senha.seq

    def __repr__(self):
        return f'{self.tipo}{self.seq}'


class TipoSenha:
    tipo: str
    seq: int = 0
    def __init__(self, tipo: str):
        self.tipo = tipo[0]
        if tipo in tipos:
            print(f'Tipo {tipo} já inserida')
            self.incrementaSeqSenha()
        else:
            self.adicionaLista(tipo)
            self.incrementaSeqSenha()

    def __repr__(self):
        return self.tipo

    def adicionaLista(self, valor):
        tipos.append(valor)

    def incrementaSeqSenha(self):
        self.seq += 1
        return self.seq



chama_senha = ChamaSenha()
chama_senha.incluiLista(Senha("A"))
chama_senha.incluiLista(Senha("B"))
chama_senha.incluiLista(Senha("C"))
chama_senha.incluiLista(Senha("C"))