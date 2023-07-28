# AGREGAÇÃO: Agregação é um tipo de associação entre classes em que uma classe contém objetos de outra classe como seus atributos, mas esses objetos podem existir **independentemente** da classe que os contém. Ou seja, a classe agregadora possui uma referência aos objetos agregados, mas não é responsável por criá-los ou gerenciá-los. Quando a classe agregadora é destruída, os objetos agregados não são necessariamente destruídos.

# A classe Pessoa usa a classe Emprego de forma 'agregada', a classe emprego pode existir e ser usada de forma externa normalmente, fora do escopo de Pessoa, por isso chamamos de classe agregada.

# Classe Emprego que vai ser agregada a Pessoa
class Emprego:
    def __init__(self):
        self.cargo = 'em treinamento'
        self.salario = 1320.0

    # métodos get para retornar os valores de cargo e salário
    def get_cargo(self):
        return self.cargo

    def get_salario(self):
        return self.salario

# Classe Pessoa que vai usar de Emprego de forma agregada
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.emprego = None

    # Método set para atribuir o valor de cargo
    def set_emprego(self, emprego: Emprego):
        self.emprego = emprego

    # Método get para retornar o valor de emprego
    def get_emprego(self):
        return self.emprego

# COMPOSIÇÃO: A composição é um tipo de associação entre classes em que uma classe contém objetos de outra classe como seus atributos, esses objetos são partes **fundamentais** da classe agregadora. Em outras palavras, a classe compositora é responsável por criar e gerenciar os objetos agregados a ela, e eles não existem independentemente dela.

# A classe Pedido usa a classe ItemPedido de forma composta, ou seja, o ItemPedido, só vai existir quando um Pedido existir, de forma que não faz sentido um ItemPedido existir sem um Pedido, por isso composição, porque ItemPedido compõe Pedido.


class ItemPedido:
    def __init__(self, produto, valor):
        self.nome = produto
        self.valor = valor


class Pedido:
    def __init__(self):
        self.cliente = 'Manoela Medeiros'
        self.item_pedido = []  # do tipo ItemPedido

    def adicionar_item(self, item_pedido: ItemPedido):
        self.item_pedido.append(item_pedido)

    def listar_pedido(self):
        print(f'Cliente: {self.cliente}')
        print('Itens do Pedido:')
        for i in range(0, len(self.item_pedido)):
            print(
                f'Nome: {self.item_pedido[i].nome}\nValor: R$ {self.item_pedido[i].valor:,.2f}')
