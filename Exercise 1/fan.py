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
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    def set_speed(self, speed):
        if speed not in (Fan.SLOW, Fan.MEDIUM, Fan.FAST):
            raise ValueError(
                f"Invalid speed '{speed}'. Use Fan.SLOW, Fan.MEDIUM, or Fan.FAST."
            )
        self.__speed = speed
        
    def set_on(self, on):
        if not isinstance(on, bool):
            raise TypeError("'on' must be a boolean value (True or False).")
        self.__on = on
    
    def set_radius(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.__radius = float(radius)
        
    def set_color(self, color):
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Color must be a non-empty string.")
        self.__color = color.strip()
    
    def turn_on(self):
        self.__on = True
    
    def turn_off(self):
        self.__on = False
        
    def increase_speed(self):
        if self.__speed < Fan.FAST:
            self.__speed += 1  
            print("Fan is already at maximum speed (FAST).")

    def decrease_speed(self):
        if self.__speed > Fan.SLOW:
            self.__speed -= 1
        else:
            print("Fan is already at minimum speed (SLOW).")
    
    def __str__(self):
        status = "ON" if self.__on else "OFF"
        return (
            f"Fan [{self.__color.upper()}] | "
            f"Speed: {self.get_speed_label()} ({self.__speed}) | "
            f"Radius: {self.__radius} in | "
            f"Status: {status}"
        )