from classes import Emprego, Pessoa
from classes import ItemPedido, Pedido

if __name__ == '__main__':
    print('Agregação'.upper())

    funcionario = Pessoa('Bruno')
    funcionario.set_emprego(Emprego())

    print(f'Funcionário: {funcionario.nome}')
    print(f'Cargo: {funcionario.get_emprego().get_cargo()}')
    print(f'Salário: R$ {funcionario.get_emprego().get_salario():,.2f}')

    print('\nComposição'.upper())

    pedido = Pedido()

    item_pedido = ItemPedido('Frango Assado', 6.99)
    pedido.adicionar_item(item_pedido)

    item_pedido = ItemPedido('Batata Frita', 5.59)
    pedido.adicionar_item(item_pedido)

    item_pedido = ItemPedido('Chocolate em Barra', 10.0)
    pedido.adicionar_item(item_pedido)

    pedido.listar_pedido()
