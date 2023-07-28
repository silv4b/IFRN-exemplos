class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

endereco_pessoa = Endereco("Rua A", 123, "Cidade X")
pessoa = Pessoa("Alice", endereco_pessoa)

# Neste exemplo, a classe Pessoa possui um atributo endereco, que é uma instância da classe Endereco. No entanto, neste exemplo, estamos considerando que o objeto endereco é uma parte fundamental da classe Pessoa, e a classe Pessoa é responsável por criar e gerenciar o objeto endereco. Quando a classe Pessoa for destruída, o objeto endereco também será destruído.
