class Animal:
   quem_sou = 'Animal'
   def som(self):
       return "Som genérico"

class Gato(Animal):
   quem_sou = 'Gato'
   def som(self):
       return "Miau"

class Cachorro(Animal):
   quem_sou = 'Cachorro'
   def som(self):
       return "Au Au"

if __name__ == '__main__':
    bicho_01 = Animal()
    print('Sou um ' + bicho_01.quem_sou + '\t| ' + bicho_01.som())

    bicho_02 = Gato()
    print('Sou um ' + bicho_02.quem_sou + '\t| ' + bicho_02.som())

    bicho_03 = Cachorro()
    print('Sou um ' + bicho_03.quem_sou + '\t| ' + bicho_03.som())


# nesse código temos o método som() sendo sobrecarregado duas vezes, tanto na classe Gato, quanto na classe Cachorro, ambas herdando de Animal, tendo comportamento específicos em cada uma das classes