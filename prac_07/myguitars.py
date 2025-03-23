from prac_07.guitar import Guitar

def load_guitars(filename):
    """Load guitars from CSV file and return list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty list.")
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for guitar in guitars:
        print(guitar)


def main():
    """Main program to manage guitar collection."""
    filename = "guitars.csv"

    guitars = load_guitars(filename)

    print("\nOriginal guitar list:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)

main()