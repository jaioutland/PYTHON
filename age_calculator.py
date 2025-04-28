def main():

    print("\n\n")
    try:
        # User inputs birth year, month, and day
        birth_year = int(input("What year were you born? "))
        birth_month = int(
            input("What month were you born (as a number, e.g., May is 5)? "))
        birth_day = int(input("What day of the month were you born? "))

        # Datetime object for the user's bday
        birth_date = datetime.date(birth_year, birth_month, birth_day)

        print(f"Your birthday is: {birth_date}")

        # Dislpay today's date
        today_date = datetime.date.today()

        # Calculate the difference between today's date user's birthdate
        age_delta = today_date - birth_date

        # Calculate years, months, weeks, days, hours, and minutes
        years = age_delta.days / 365.25
        months = (age_delta.days % 365) // 30
        weeks = age_delta.days // 7
        days = age_delta.days
        hours = days * 24
        minutes = hours * 60

        print(f"\nDifference is {days} days")
        print(f"You are {years:.2f} years old")
        print(f"You are {months} months old")
        print(f"You are {weeks} weeks old")
        print(f"You are {days} days old")
        print(f"You are {hours} hours old")
        print(f"You are {minutes} minutes old")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Run main
if __name__ == "__main__":
    main()
