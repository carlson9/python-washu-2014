class BiologicalThing(object):    #class definition - object is default, inherits from object
    def alive(self):
        return True

class Animal(BiologicalThing):
    def __init__(self, age):
        self.age = age
    def gets_energy_dirdctly_from_the_sun(self):
        return False

class Plant(BiologicalThing):
    def gets_energy_dirdctly_from_the_sun(self):
        return True

class Mammal(Animal):
    def __init__(self, age, sex):
        Animal.__init__(self, age)
        self.sex = sex

    def has_hair(self):
        return True

    def has_live_births(self):
        return True

class Human(Mammal):
    def __init__(self, age, sex, name): #initializer or contructor
        Mammal.__init__(self, age, sex)
        self.name = name
    
    def speak(self, words):
        if self.sex=="Male": return words.upper()
        else: return words

    def introduce(self):
        return self.speak("Hello, I'm %s" % self.name)

andy = Human(21, "Male", "Andy")

print andy.introduce()
