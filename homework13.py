'''
Homework13
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/homework13.py
'''
def calculate_interest(principal, rate, time):
    interest = principal * rate * time  # Calculate interest
    return int(interest)


def compound_interest(principal, rate, compounded_per_year, time): # Calculate compound interest
    amount = principal * (1 + (rate / compounded_per_year)) ** (compounded_per_year * time)
    return round(amount, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest13.py'))