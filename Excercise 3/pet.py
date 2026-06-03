VALID_TYPES = {"Dog", "Cat", "Bird", "Fish", "Rabbit",
               "Hamster", "Turtle", "Snake", "Lizard", "Other"}

class Pet:
    def __init__(self, name: str = "", animal_type: str = "", age: int = 0):
        self.__name        = ""
        self.__animal_type = ""
        self.__age         = 0
        
        if name:
            self.set_name(name)
        if animal_type:
            self.set_animal_type(animal_type)
        if age:
            self.set_age(age)