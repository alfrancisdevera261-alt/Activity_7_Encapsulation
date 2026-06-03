class Car:
    
    SPEED_INCREMENT = 5    # how many mph are added each time we accelerate
    SPEED_DECREMENT = 5    # how many mph are removed each time we brake
    MIN_SPEED       = 0    # a car cannot have negative speed
    MAX_SPEED       = 200  # safety ceiling — no car goes faster than this
