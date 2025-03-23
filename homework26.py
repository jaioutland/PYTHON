'''
Homework24
Name:Jai Outland
github link:
'''


def dictionary_exceptions(key, flower_dict):
    try:     # Check if key not valid flower name
        if not isinstance(key, str) or key.strip() == "" or key not in flower_dict:
            print("Error: Flower not found! Please enter Rose, Lily, or Tulip.")
            return  # Avoid execution if key is invalid

        # Price will print if key is valid
        print(f"The price of {key} is ${flower_dict[key]}")

    except KeyError:
        print("Error: Flower not found! Please enter Rose, Lily, or Tulip.")


def string_exceptions(idx, text):
    try:  # Check if index is not an integer
        if not isinstance(idx, int):
            raise TypeError(
                f"Error: String indices must be integers, not '{type(idx).__name__}'")
        if idx < 0 or idx >= len(text):
            raise IndexError(
                "Error: Index out of range! Please enter a valid index.")

        print(f"The character at index {idx} is: {text[idx]}")

    except (TypeError, IndexError) as e:   # Display error message if exception occurs
        print(str(e))


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest26.py'))
