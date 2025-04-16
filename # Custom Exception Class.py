
class InvalidInputError(Exception):
    # Populates when input isn't a numeric value
    pass

# Main function


def main():
    while True:
        try:
            user_input = input("Enter a number: ")

            if not user_input.isnumeric():
                raise InvalidInputError("Input must be a number.")

        except InvalidInputError as e:
            # Handle custom error
            print(f"Error: {e}")

        else:
            # If no exception is raised, input is valid
            print(f"Thank you! You entered a valid number: {user_input}")
            break  # Exit loop

        finally:
            print("Attempt to validate input complete.\n")


# Call main function
main()
