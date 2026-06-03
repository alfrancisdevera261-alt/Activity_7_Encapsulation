class Fan:
    #speed settings
    SLOW   = 1  
    MEDIUM = 2  
    FAST   = 3   
    
    _SPEED_LABELS = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}
    
    def __init__(self, speed=None, radius=5.0, color="blue", on=False):
        if speed is None:
            speed = Fan.SLOW
        
        self.__speed  = None
        self.__radius = None
        self.__color  = None
        self.__on     = None
        
        self.set_speed(speed)
        self.set_radius(radius)
        self.set_color(color)
        self.set_on(on)
        
    def get_speed(self):
        return self.__speed
    
    def get_speed_label(self):
        return Fan._SPEED_LABELS.get(self.__speed, "UNKNOWN")
    
    def get_on(self):
        return self.__on