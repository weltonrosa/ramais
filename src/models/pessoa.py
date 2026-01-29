class Pessoa:
    def __init__(self, nome: str, sobrenome: str , idade: int, ramal: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.ramal = ramal

    def nome_completo(self) -> str:
        return f'{self.nome} {self.sobrenome}'

    def apresentar(self) -> str:
        return f'Olá, meu nome é {self.nome} {self.sobrenome} e tenho {self.idade} anos. Meu ramal é {self.ramal}.'