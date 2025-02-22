"""
Emails
Estimate: 20 minutes
Actual:   36 minutes
"""

def main():
    """Store users' emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()

    while email:

        name = extract_name(email)
        correct_name = input(f"Is your name {name}? (Y/n): ").strip().lower()

        if correct_name not in ['n', 'no']:
            email_to_name[email] = name
        else:
            name = input("Name: ").strip()
            email_to_name[email] = name

        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email address."""
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    name = ' '.join(name_parts).title()
    return name




main()
