def birthday(month,day,year):
    return f" Your birthday is: {month}/ {day}/ {year}"
print(birthday("September", 12, 1988))
print()


def address(street,city,state,zipcode):
    return  f" Your address is: {street}, {city}, {state}, {zipcode}"
print(address("435 W 35 St.", "New York", "NY", 11462))
print()


if __name__ == "__main__":
    print(birthday("\nMay", 10, 1956))
    print(birthday("\nDeember", 21, 2002))
    print(birthday("\nJune", 8, 2013))
    print(address("\n123 Main St", "Starfall", "AZ", 60547))
    print(address("\n45 On Lookers Lane", "Ashland", "IL", 98014))
    print(address("\n845w Mistwwd Ct", "Springfield", "MI", 45017))