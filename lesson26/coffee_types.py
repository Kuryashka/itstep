from abc import ABC, abstractmethod
class Coffee(ABC):

    @abstractmethod
    def get_cup_size(self):
        pass

    @abstractmethod
    def is_have_milk(self):
        pass

    @abstractmethod
    def coffee_name(self):
        pass

class Latte(Coffee):
    
    name = ''

    def __init__(self, name):
        self.name = name

    def get_cup_size(self):
        cup_size = '500 ml'
        print(cup_size)
    
    def is_have_milk(self):        
        milk = True
        print(milk)

    def coffee_name(self):        
        name = "latte"
        print(name)


class Cappucino(Coffee):

    name = ''

    def __init__(self, name):
        self.name = name

    def get_cup_size(self):
        cup_size = '250 ml'
        print(cup_size)
    
    def is_have_milk(self):        
        milk = True
        print(milk)

    def coffee_name(self):        
        name = "cappucino"
        print(name)

class Black(Coffee):

    name = ''

    def __init__(self, name):
        self.name = name

    def get_cup_size(self):
        cup_size = '200 ml'
        print(cup_size)

    def is_have_milk(self):        
        milk = False
        print(milk)

    def coffee_name(self):        
        name = "black"
        print(name)

class Espresso(Coffee):
    
    name = ''

    def __init__(self, name):
        self.name = name

    def get_cup_size(self):
        cup_size = '350 ml'
        print(cup_size)

    def is_have_milk(self):        
        milk = False
        print(milk)

    def coffee_name(self):        
        name = "espresso"
        print(name)

class Mocha(Coffee):

    name = ''

    def __init__(self, name):
        self.name = name

    def get_cup_size(self):
        cup_size = '250 ml'
        print(cup_size)

    def is_have_milk(self):        
        milk = True
        print(milk)

    def coffee_name(self):        
        name = "mocha"
        print(name)


    

if __name__ == '__main__':
    latte = Latte('cup one')
    latte.is_have_milk()
    latte.get_cup_size()
    latte.coffee_name()

    cappucino = Cappucino('cup two')
    cappucino.get_cup_size()
    cappucino.is_have_milk()
    cappucino.coffee_name()

    black = Black('cup three')
    black.get_cup_size()
    black.is_have_milk()
    black.coffee_name()

    espresso = Espresso('cup four')
    espresso.get_cup_size()
    espresso.is_have_milk()
    espresso.coffee_name()
    
    mocha = Mocha('cup five')
    mocha.get_cup_size()
    mocha.is_have_milk()
    mocha.coffee_name()
