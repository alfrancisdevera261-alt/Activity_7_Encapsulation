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

    def set_name(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = name.strip().title()
    
    def set_animal_type(self, animal_type: str):
        if not isinstance(animal_type, str) or not animal_type.strip():
            raise ValueError("Animal type must be a non-empty string.")
        
        normalised = animal_type.strip().title()

        if normalised in VALID_TYPES:
            self.__animal_type = normalised
        else:
            print(
                f"  ℹ  '{animal_type}' is not in the known types list. "
                f"Storing as-is."
            )
            self.__animal_type = normalised
    
    def set_age(self, age: int):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.__age = age
    
    def get_name(self) -> str:
        return self.__name

    # STEP 7: Getter for animal type.
    def get_animal_type(self) -> str:
        return self.__animal_type

    # STEP 8: Getter for age.
    def get_age(self) -> int:
        return self.__age