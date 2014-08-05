class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self): #all subclasses must have talk method
        raise NotImplementedError("Subclass must implement abstract method.")
