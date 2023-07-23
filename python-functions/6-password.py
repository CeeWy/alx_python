def validate_password(password):
    if len(password) < 8:
        return False
    if ' ' in password:
        return False
    # Check for uppercase, lowercase, and digits
    upperCase = False
    lowerCase = False
    digit = False

    for char in password:
        if char.isupper():
            upperCase = True
        elif char.islower():
            lowerCase = True
        elif char.isdigit():
            digit = True
    if upperCase and lowerCase and digit:
        return True
    else:
        return False