# AGREGAÇÃO: Relacionamento onde o objeto “agregado” a outro faz sentido sozinho (mesmo sem ser parte do objeto que o contém).

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

# A classe Pessoa usa a classe Emprego de forma 'agregada', semanticamente, a classe emprego pode existir e ser usada normalmente fora do escopo de Pessoa, por isso chamamos de classe agregada.

# ======================================================

# COMPOSIÇÃO: Relacionamento “mais restritivo” que a agregação onde o objeto que compõe outro não faz sentido sozinho (sem fazer parte do objeto que o contém)


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

# A classe Pedido usa a classe ItemPedido de forma composta, ou seja, o ItemPedido, só vai existir quando um Pedido existir, de forma que não faz sentido um ItemPedido existir sem um pedido, por isso composição, porque ItemPedido compõe Pedido
