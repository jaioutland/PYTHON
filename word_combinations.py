
# Function that yields all possible two-letter combinations


def two_letter_combinations(characters):
    for first in characters:
        for second in characters:
            yield first + second  # Yield will pause function to return the value

# Define 5 letter list


def main():
    chars = ['b', 'e', 'k', 'j', 'm']

# Call and print two-letter combination function
    print("All possible two-letter combinations:")
    for combo in two_letter_combinations(chars):
        print(combo)


# Call main function
main()
