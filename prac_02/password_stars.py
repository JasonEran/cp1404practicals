PASSWORD_LENGTH = 10
password = input('Enter a password: ')
while len(password) < PASSWORD_LENGTH:
    print(f'Password must be at least {PASSWORD_LENGTH} characters long.')
    password = input('Enter a password: ')
print("*" * len(password))