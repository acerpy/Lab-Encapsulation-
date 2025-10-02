class Mammal:
    __kingdom = "animals" # private clas attribute
    def __init__(self, name, type, sound):
        self.name = name # public attribute
        self.type = type # public attribute
        self.sound = sound # public attribute
    
    def make_sound(self): # public method
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self): # public method
        return self.__kingdom # access private class attribute
    
    def info(self): # public method
        return f"{self.name} is of type {self.type}"
    
mammal = Mammal("Dog", "Domestic", "Bark") 
print(mammal.make_sound()) 
print(mammal.get_kingdom()) 
print(mammal.info()) 