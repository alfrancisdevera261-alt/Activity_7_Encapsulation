from pet import Pet, VALID_TYPES
def print_separator(title=""):
    width = 55
    if title:
        padding = (width - len(title) - 2) // 2
        print("=" * padding + f" {title} " + "=" * padding)
    else:
        print("=" * width)
    
def prompt_name() -> str:
    while True:
        name = input("  Enter your pet's name: ").strip()
        
        if name:
            return name
        print("  ⚠  Name cannot be empty. Try again.")
    
def prompt_animal_type() -> str:
    known = sorted(VALID_TYPES)
    print(f"\n  Known types: {', '.join(known)}")
    while True:
        animal_type = input("  Enter your pet's animal type: ").strip()
        if animal_type:
            return animal_type
        print("  ⚠  Animal type cannot be empty. Try again.")

def prompt_age() -> int:
    while True:
        raw = input("  Enter your pet's age (in years): ").strip()
        if raw.isdigit():
            return int(raw)
        print("  ⚠  Age must be a whole non-negative number. Try again.")