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