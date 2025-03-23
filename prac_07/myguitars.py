"""
CP1404/CP5632 Practical
My Guitars
"""

from prac_07.guitar import Guitar, CURRENT_YEAR

FILENAME = "guitars.csv"

def main():
    """Main program to manage guitar collection."""
    guitars = load_guitars(FILENAME)

    print("\nOriginal guitar list:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)

    print("\nEnter new guitars (blank name to finish)")
    guitars = add_guitars_recursively(guitars)

    save_guitars(FILENAME, guitars)

    print("\nFinal guitar list:")
    guitars.sort()
    display_guitars(guitars)

def load_guitars(filename):
    """Load guitars from CSV file and return list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as in_file:
            for line in in_file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty list.")
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for guitar in guitars:
        print(guitar)


def get_valid_year():
    """Get a valid year from user with recursion."""
    try:
        year = int(input("Year: "))
        if 0 <= year <= CURRENT_YEAR:
            return year
        print(f"Invalid year. Must be between 0 and {CURRENT_YEAR}")
        return get_valid_year()
    except ValueError:
        print(f"Invalid year. Must be between 0 and {CURRENT_YEAR}")
        return get_valid_year()


def get_valid_cost():
    """Get a valid cost from user with recursion."""
    try:
        cost = float(input("Cost: $"))
        if cost >= 0:
            return cost
        print("Cost must be a positive number")
        return get_valid_cost()
    except ValueError:
        print("Cost must be a positive number")
        return get_valid_cost()


def get_new_guitar():
    """Get details for a new guitar from user."""
    name = input("Name: ")
    if not name:
        return None
    year = get_valid_year()
    cost = get_valid_cost()
    return Guitar(name, year, cost)


def add_guitars_recursively(guitars):
    """Recursively add new guitars to the list."""
    new_guitar = get_new_guitar()
    if new_guitar is None:
        return guitars
    guitars.append(new_guitar)
    return add_guitars_recursively(guitars)


def save_guitars(filename, guitars):
    """Save all guitars to CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()