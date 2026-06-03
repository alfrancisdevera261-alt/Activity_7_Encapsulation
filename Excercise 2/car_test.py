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
    
    print()
    print_separator("BRAKING  ×5")
    print()
    for i in range(1, 6):
        # Step 7a: Call brake() — this decreases __speed by 5 inside the object.
        new_speed = my_car.brake()
        # Step 7b: Display the loop counter and the new speed as a progress bar.
        print(f"  Brake #{i}  {speed_bar(new_speed)}")
        
    print()
    print_separator("FINAL STATS")
    stats = my_car.get_stats()   # call the stats getter
    print(f"\n  Car                 : {stats['year_model']} {stats['make']}")
    print(f"  Final Speed         : {stats['speed']} mph")
    print(f"  Total Accelerations : {stats['total_accelerations']}")
    print(f"  Total Brakes        : {stats['total_brakes']}")

    print()
    print_separator("EXTRAS")
    print()

    for _ in range(4):
        my_car.accelerate()
    print(f"  After accelerating 4 more times: {my_car.get_speed()} mph")

    my_car.full_stop()
    print(f"  Speed after full stop: {my_car.get_speed()} mph")
    
    print()
    try:
        bad_car = Car(year_model=1800, make="Horse Carriage")
    except ValueError as e:
        print(f"  [ValueError caught] {e}")

    print_separator()
    print("  All tests complete.\n")

if __name__ == "__main__":
    main()
