# INTERFACE

from abc import ABCMeta, abstractmethod, ABC


class Conta(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, numero: str = "00000", titular: str = "root", saldo: float = 0.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    @abstractmethod
    def sacar(self, value: float):
        pass

    @abstractmethod
    def depositar(self, value: float):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass


class ContaCorrente(Conta, ABC):
    def __init__(self, numero: str = "00000", titular: str = "root", saldo: float = 0.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    def sacar(self, value: float):
        pass

    def depositar(self, value: float):
        pass

    def exibir_saldo(self):
        pass


if __name__ == '__main__':
    conta = ContaCorrente()
