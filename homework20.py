# Converts strings to ASCII Value

def convert_to_ascii(string):
    if len(string) == 1:
        raise ValueError("Enter a single character.")
    return ord(char)


# Filters non-ASCII characters from a string

def filter_non_ascii(string):
    return "".join(char for char in string if ord(char) < 128).strip()


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))
