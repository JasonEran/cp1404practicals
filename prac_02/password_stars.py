PASSWORD_LENGTH = 10
def main():
    password = input(f'Enter a password (at least {PASSWORD_LENGTH} characters): ')
    while len(password) < PASSWORD_LENGTH:
        print(f'Password must be at least {PASSWORD_LENGTH} characters long.')
        password = input('Enter a password: ')
    print("*" * len(password))

main()