'''
Homework24
Name: Jai Outland
github link: 
'''


def is_valid_password(word):
    if len(word) < 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

# Checking for each character in password

    for char in word:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  # Special character check
            has_special =True

# Will return True if all conditions are met

    return has_lower and has_upper and has_digit and has_special

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest24.py'))
