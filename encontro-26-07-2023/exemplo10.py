class Pessoa:
    def falar(self):
        print('Voz Genérica')
    
class Mulher(Pessoa):
    # sobrecarga
    def falar(self):
        print('Voz "fina"')

class Homem(Pessoa):
    # sobrecarga
    def falar(self):
        print('Mudo')

if __name__ == '__main__':
    m = Mulher()
    m.falar()

    h = Homem()
    h.falar()

# nesse código temos o método falar() sendo sobrecarregado duas vezes, tanto na classe Mulher, quanto na classe Homem, tendo comportamento específicos em cada uma das classes