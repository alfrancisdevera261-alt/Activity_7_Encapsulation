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