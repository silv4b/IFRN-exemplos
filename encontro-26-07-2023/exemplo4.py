class Teste:
    a = 1 # publico
    _b = 2 # protegido (convenção)
    __c = 3 # private


if __name__ == '__main__':
    t = Teste()
    print(t._)
    print(t.__c)
