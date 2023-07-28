class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

motor_carro = Motor(150)
carro = Carro("Fiat", motor_carro)

# Neste exemplo, a classe Carro possui um atributo motor, que é uma instância da classe Motor. A classe Carro pode utilizar o objeto motor (como o valor de potencia) durante sua execução. No entanto, o objeto motor pode existir independentemente do objeto carro, e não é criado ou gerenciado pela classe Carro.
