class Animal:
   quem_sou = 'Sou um Animal'
   def som(self):
       return "Som genérico"

class Gato(Animal):
   def som(self):
       return "Miau"

class Cachorro(Animal):
   def som(self):
       return "Auau"

if __name__ == '__main__':
    bicho_01 = Animal()
    print(bicho_01.quem_sou + ' | ' + bicho_01.som())

    bicho_02 = Gato()
    print(bicho_02.quem_sou + ' | ' + bicho_02.som())

    bicho_03 = Cachorro()
    print(bicho_03.quem_sou + ' | ' + bicho_03.som())
