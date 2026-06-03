class Car:
    
    SPEED_INCREMENT = 5    # how many mph are added each time we accelerate
    SPEED_DECREMENT = 5    # how many mph are removed each time we brake
    MIN_SPEED       = 0    # a car cannot have negative speed
    MAX_SPEED       = 200  # safety ceiling — no car goes faster than this

    def __init__(self, year_model: int, make: str):
        if not isinstance(year_model, int) or year_model < 1886:
            raise ValueError("Year model must be an integer >= 1886.")