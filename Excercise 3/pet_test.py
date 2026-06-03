from pet import Pet, VALID_TYPES
def print_separator(title=""):
    width = 55
    if title:
        padding = (width - len(title) - 2) // 2
        print("=" * padding + f" {title} " + "=" * padding)
    else:
        print("=" * width)