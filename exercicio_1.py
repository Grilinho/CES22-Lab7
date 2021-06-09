# Aluno: Gabriel Teixeira Rodrigues
# CES-22: Programação Orientada a Objetos
# Professora Karla Donato Fook   

class Pizza:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class MassaTradicional(Pizza):
    cost = 5.0

class Decorator(Pizza):
    def __init__(self, pizza):
        self.component = pizza

    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + Pizza.getDescription(self)

class BordaCatupiry(Decorator):
    cost = 2.50
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class BordaCheddar(Decorator):
    cost = 3.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Frango(Decorator):
    cost = 5.0
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Bacon(Decorator):
    cost = 3.25
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Cebola(Decorator):
    cost = 1.50
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Calabresa(Decorator):
    cost = 2.25
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Palmito(Decorator):
    cost = 4.75
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Tomate(Decorator):
    cost = 1.50
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Mussarela(Decorator):
    cost = 3.75
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Catupiry(Decorator):
    cost = 3.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Presunto(Decorator):
    cost = 2.50
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Ovo(Decorator):
    cost = 1.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

pizza1 = Frango(Catupiry(Mussarela(BordaCatupiry(MassaTradicional()))))
print(pizza1.getDescription()+ ": $" + str(pizza1.getTotalCost()))

pizza2 = Bacon(Presunto(Ovo(Tomate(Palmito(BordaCheddar(MassaTradicional()))))))
print(pizza2.getDescription()+ ": $" + str(pizza2.getTotalCost()))