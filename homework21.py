'''
Homework21
Name: Jai Outland
github link: 
'''

# Remove alphanumeric characters


def is_palindrome(string):
    filter_string = []
    for char in string:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            filter_string.append(char.lower())
    return str("".join(filter_string)) == str("".join(filter_string[::-1]))


# Process both strings by removing alphanumeric characters and convert to lowercase

def is_anagram(string1, string2):
    filter_string1 = []
    filter_string2 = []

    for char in string1:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            filter_string1.append(char.lower())

    for char in string2:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            filter_string2.append(char.lower())

    return sorted(filter_string1) == sorted(filter_string2)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))
