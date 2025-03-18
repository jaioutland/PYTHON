# Converts strings to ASCII Value

def convert_to_ascii(string):
 if len(string) == 1:
        return ord(string)
    elif len(string) > 1:
        raise ValueError("Enter a single character.")

# Filters non-ASCII characters from a string

def filter_non_ascii(string):
    filter_chars = []
    for char in string:
        if ord(char) < 128:
            filter_chars.append(char)
    return str("".join(filter_chars)).strip()


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))
