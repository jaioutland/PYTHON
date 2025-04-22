"""
The program reads sales totals in a file to calculate
the total and count the average
"""


def main():
    try:
        # Open file and read all lines
        with open("sales_totals.txt", "r") as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            amount = float(line.strip())
            total += amount
            count += 1
            print(f"{amount:,.2f}")

        # Print final results
        print(f"\nTotal: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {total / count:,.2f}" if count else "Average: 0.00")

    except FileNotFoundError:
        print("File not found.")

    except ValueError:
        print("Bad data in file. Make sure all lines are valid numbers.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call main function
main()
