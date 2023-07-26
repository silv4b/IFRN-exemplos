class Pessoa:
    def falar(self):
        print('Voz Genérica')
    
class Mulher(Pessoa):
    # sobrecarga
    def falar(self):
        print('Voz "fina"')

class Homem(Pessoa):
    def falar(self):
        print('Mudo')

if __name__ == '__main__':
    h = Homem()
    h.falar()
