PASSWORD_LENGTH = 10
def main():
    password = get_password()
    while len(password) < PASSWORD_LENGTH:
        print(f'Password must be at least {PASSWORD_LENGTH} characters long.')
        password = input('Enter a password: ')
    print_password(password)

def print_password(password):
    print("*" * len(password))

def get_password():
    password = input(f'Enter a password (at least {PASSWORD_LENGTH} characters): ')
    return password

main()
