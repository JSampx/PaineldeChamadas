class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ChamaSenha(metaclass=SingletonMeta):
    contador: int = 0
    lista: list = []

    def incluiLista(self, senha):
        if senha in self.lista:
            print(f'A senha {senha} já existe na lista')
        else:
            self.lista.append(senha)
            self.contador += 1
        print(self.lista)


class TipoSenha:
    _tipos = {}

    def __init__(self, tipo: str):
        self.tipo = tipo
        if tipo not in TipoSenha._tipos:
            TipoSenha._tipos[tipo] = 1
        else:
            print(f'Tipo {tipo} já inserido.')

    @classmethod
    def geraSenha(cls, tipo: str):
        if tipo not in cls._tipos:
            cls._tipos[tipo] = 1
        else:
            cls._tipos[tipo] += 1
        return f'{tipo}{cls._tipos[tipo]}'

chama_senha = ChamaSenha()
chama_senha.incluiLista(TipoSenha.geraSenha("A"))
chama_senha.incluiLista(TipoSenha.geraSenha("B"))
chama_senha.incluiLista(TipoSenha.geraSenha("C"))
chama_senha.incluiLista(TipoSenha.geraSenha("C"))
chama_senha.incluiLista(TipoSenha.geraSenha("C"))