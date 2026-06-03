from car import Car

def print_separator(title=""):
    width = 55
    if title:
        padding = (width - len(title) - 2) // 2
        print("=" * padding + f" {title} " + "=" * padding)
    else:
        print("=" * width)

def speed_bar(speed, max_speed=200, bar_width=30):
    filled = int((speed / max_speed) * bar_width)
    bar = "█" * filled + "░" * (bar_width - filled)
    return f"[{bar}] {speed:>3} mph"

def main():
    print_separator("CAR CLASS DEMO")
    
    my_car = Car(year_model=2024, make="Toyota GR86")

    print(f"\n  Vehicle  : {my_car.get_make()}")        
    print(f"  Year     : {my_car.get_year_model()}")    
    print(f"  Speed    : {my_car.get_speed()} mph\n")  
    
    print_separator("ACCELERATING  ×5")
    print()
    for i in range(1, 6):
        new_speed = my_car.accelerate()
        print(f"  Accel #{i}  {speed_bar(new_speed)}")
    
