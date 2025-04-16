from employee import ProductionWorker


def main():
    print("\nWelcome to the Production Worker Info System\n")

# Employee information Prompt
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")

# Shift validation
    while True:
        try:
            shift = int(input("Enter shift number (1 for Day, 2 for Night): "))
            if shift in (1, 2):
                break
            else:
                print("Please enter 1 for Day or 2 for Night.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    # Employee pay rate prompt for validation
    try:
        pay_rate = float(input("Enter hourly pay rate: "))
        if pay_rate < 0:
            print("Hourly pay rate cannot be negative. Setting to $0.00.")
            pay_rate = 0.00
    except ValueError:
        print("Invalid input. Setting hourly pay rate to $0.00.")
        pay_rate = 0.00

    worker = ProductionWorker(name, number, shift, pay_rate)

    print("\nEmployee Created Successfully!\n")
    print(worker)

    # Pay rate feedback
    if pay_rate > 50:
        print("Note: This is a high-paying position!")
    elif pay_rate < 15:
        print("Note: This is below the average wage.")

    print("\nThank you!\n")


# Call main function
main()
