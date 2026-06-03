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
    
    def age_description(self) -> str:
        a = self.__age
        t = self.__animal_type.lower()  

        if t in ("dog", "cat"):
            if a <= 1:  return "baby (< 1 yr)"
            if a <= 3:  return "young adult"
            if a <= 8:  return "adult"
            return "senior"
        
        elif t == "bird":
            if a <= 1:  return "chick/fledgling"
            if a <= 5:  return "juvenile"
            return "mature"
        
        else:
            if a == 0:  return "newborn"
            # "year" vs "years" — handle singular correctly.
            return f"{a} year{'s' if a != 1 else ''} old"
    
    def __str__(self) -> str:
        return (
            f"Pet: {self.__name} | "
            f"Type: {self.__animal_type} | "
            f"Age: {self.__age} yr(s) [{self.age_description()}]"
        )

    # STEP 11: __repr__ is used by the debugger — shows constructor-like form.
    def __repr__(self) -> str:
        return (
            f"Pet(name='{self.__name}', "
            f"animal_type='{self.__animal_type}', "
            f"age={self.__age})"
        )
