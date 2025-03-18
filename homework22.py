'''
Homework22
Name: Jai Outland
github link: 
'''

# Mask all but the last four digits


def mask_creditcard(string):
    if len(string) <= 4:
        return string
    mask_part = '*' * (len(string) - 4)
    last_four = string[-4:]
    return mask_part + last_four

# Remove all vowels from the string


def remove_vowels(string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest22.py'))
