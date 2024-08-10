def password_validator(password):
    is_valid = True

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        is_valid = False

    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        is_valid = False

    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        is_valid = False

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        is_valid = False

    if not any(not char.isalnum() for char in password):
        print("Password must contain at least one special character.")
        is_valid = False

    if is_valid:
        print("Password is valid.")

password = input("Enter a password: ")
password_validator(password)