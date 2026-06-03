from fan import Fan

def print_separator(title=""):
    width = 55
    if title:
        padding = (width - len(title) - 2) // 2
        print("=" * padding + f" {title} " + "=" * padding)
    else:
        print("=" * width)

def display_fan(label, fan):
    print(f"\n  {label}")
    print(f"  {'-' * 45}")
    print(f"  Color   : {fan.get_color()}")
    print(f"  Speed   : {fan.get_speed_label()} (value = {fan.get_speed()})")
    print(f"  Radius  : {fan.get_radius()} inches")
    print(f"  Status  : {'ON ✔' if fan.get_on() else 'OFF ✘'}")
    print(f"  {fan}")
    
def main():
    print_separator("FAN CLASS DEMO")
    fan1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)
    fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)
    print("\n[ Initial Fan Configurations ]\n")
    display_fan("Fan 1", fan1)
    display_fan("Fan 2", fan2)