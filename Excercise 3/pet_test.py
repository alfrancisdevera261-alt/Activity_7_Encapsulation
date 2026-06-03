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

def display_pet(my_pet: Pet):
    print()
    print_separator("YOUR PET'S INFO")
    print()
    print(f"  Name        : {my_pet.get_name()}")
    print(f"  Animal Type : {my_pet.get_animal_type()}")
    print(f"  Age         : {my_pet.get_age()} year(s)")
    print(f"  Life Stage  : {my_pet.age_description()}")
    print()
    print(f"  Summary → {my_pet}")
    print()

def demo_setters(my_pet: Pet):
    print_separator("DEMO: Updating via Setters")
    print()

    original_age = my_pet.get_age()

    my_pet.set_age(original_age + 1)
    print(f"  Happy birthday {my_pet.get_name()}! "
          f"Age updated: {original_age} → {my_pet.get_age()}")

    print()

    try:
        my_pet.set_age(-3)
    except ValueError as e:
        print(f"  [ValueError caught] {e}")

    print()

    try:
        my_pet.set_name("")
    except ValueError as e:
        print(f"  [ValueError caught] {e}")

    print()
    
def main():
    print_separator("PET CLASS DEMO")
    print()

    my_pet = Pet()

    print("  Let's register your pet!\n")
    my_pet.set_name(prompt_name())               # stores in __name
    my_pet.set_animal_type(prompt_animal_type()) # stores in __animal_type
    my_pet.set_age(prompt_age())                 # stores in __age

    display_pet(my_pet)

    demo_setters(my_pet)