import calendar
import datetime

# Define main function


def main():

    current_year = datetime.datetime.now().year

    # User must input birth month
    while True:
        try:
            birth_month = int(input(
                "Enter your birth month (as 1 for January, 12 for December): "))

            # Authenticate month
            if 1 <= birth_month <= 12:
                break
            else:
                print("Please enter a valid month number between 1 and 12.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12.")

    # Display calendar for selected month and current year
    print(
        f"\nHere is the calendar for your birth month ({calendar.month_name[birth_month]}) in the year {current_year}:\n")

    month_calendar = calendar.month(current_year, birth_month)
    print(month_calendar)

    # User inputs birthday
    while True:
        try:
            birth_day = int(input(
                f"Enter your birth day (1-{calendar.monthrange(current_year, birth_month)[1]}): "))
            month_days = calendar.monthrange(current_year, birth_month)[1]

            if 1 <= birth_day <= month_days:
                break
            else:
                print(
                    f"Invalid day. {calendar.month_name[birth_month]} has only {month_days} days.")

        except ValueError:
            print("Invalid input. Please enter a valid day number.")

    # Bonus to make it more fun
    print(
        f"\nYou selected: {calendar.month_name[birth_month]} {birth_day}, {current_year}")
    print("🎉 Happy Birthday! 🎉")

    today = datetime.datetime.now()
    if today.month == birth_month and today.day == birth_day:
        print("🎂 Today is your Birthday! 🎂")


# Run main
if __name__ == "__main__":
    main()
