class Fan:
    #speed settings
    SLOW   = 1  
    MEDIUM = 2  
    FAST   = 3   
    
    _SPEED_LABELS = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}
    
    def __init__(self, speed=None, radius=5.0, color="blue", on=False):
        if speed is None:
            speed = Fan.SLOW