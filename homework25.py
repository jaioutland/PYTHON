def flowers(idx, list_of_flowers):
    try:
        if not isinstance(idx, int):
            raise TypeError("Invalid input! Please enter a number.")

        if idx < -len(list_of_flowers) or idx >= len(list_of_flowers):
            raise IndexError(
                "Number out of range! Please choose a valid flower number.")

        print(f"You selected: {list_of_flowers[idx]}")

    except (TypeError, IndexError)as e:
        print(str(e))


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))
