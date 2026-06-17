class Car:
    
    SPEED_INCREMENT = 5    # how many mph are added each time we accelerate
    SPEED_DECREMENT = 5    # how many mph are removed each time we brake
    MIN_SPEED       = 0    # a car cannot have negative speed
    MAX_SPEED       = 200  # safety ceiling — no car goes faster than this

    def __init__(self, year_model: int, make: str):
        if not isinstance(year_model, int) or year_model < 1886:
            raise ValueError("Year model must be an integer >= 1886.")
        
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Make must be a non-empty string.")
        
        self.__year_model = year_model
        self.__make       = make.strip()  
        self.__speed      = 0             

        self.__total_accelerations = 0
        self.__total_brakes        = 0
        
    def get_year_model(self) -> int:
        return self.__year_model
    
    def get_make(self) -> str:
        return self.__make
    
    def get_speed(self) -> int:
        return self.__speed
    
    def get_stats(self) -> dict:
        return {
            "year_model"          : self.__year_model,
            "make"                : self.__make,
            "speed"               : self.__speed,
            "total_accelerations" : self.__total_accelerations,
            "total_brakes"        : self.__total_brakes,
        }
        
    def set_year_model(self, year_model: int):
        if not isinstance(year_model, int) or year_model < 1886:
            raise ValueError("Year model must be an integer >= 1886.")
        self.__year_model = year_model
    
    def set_make(self, make: str):
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Make must be a non-empty string.")
        self.__make = make.strip()
        
    def accelerate(self) -> int:
        self.__speed = min(self.__speed + Car.SPEED_INCREMENT, Car.MAX_SPEED)
        self.__total_accelerations += 1
        return self.__speed

    def brake(self) -> int:
        self.__speed = max(self.__speed - Car.SPEED_DECREMENT, Car.MIN_SPEED)
        self.__total_brakes += 1
        return self.__speed

    def full_stop(self):
        self.__speed = 0
        print(f"  🛑 {self.__make} came to a full stop.")
        
    def __str__(self) -> str:
        return (
            f"{self.__year_model} {self.__make} | "
            f"Speed: {self.__speed} mph"
        )

    def __repr__(self) -> str:
        return (
            f"Car(year_model={self.__year_model}, "
            f"make='{self.__make}', speed={self.__speed})"
        )