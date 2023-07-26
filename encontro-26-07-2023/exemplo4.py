class Teste:
    a = 1 # atributo publico
    _b = 2 # atributo protegido (convenção)
    __c = 3 # atributo privado

    # Método Privado - Só pode ser usado dentro da classe onde existe
    def __teste(self):
        print('Print Teste')

    # Método público que chama o método privado
    def teste(self):
        self.__teste() # método privado


if __name__ == '__main__':
    t = Teste()
    print(t._b) # Funciona pois é uma convenção
    # print(t.__c) # Não funciona pois c é um atributo privado

    t.teste() # chamada de método público
