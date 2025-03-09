'''
Homework1
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/homework1.py
'''

import random

def check(guess, actual_number):   # Check function 
    if guess == 1:
        return "You Got It!"
    elif guess <=4:
        return "Very Hot!"
    elif guess <= 6:
        return "Hot"
    elif guess <=8:
        return "Cool"
    else:
        return "Cold"
    True
    
def main(actual_number):    # Main function
    while True:
        try:
            guess = int(input("Enter your guess (1-100):"))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
            result = check(guess,actual_number)
            print(result)
            if result == "You Got It!":
                break
        except ValueError:
                print("Please enter valid integer.")
    True

actual_number = random.randint(1,100)  # Random number generates between 1 and 100
main(actual_number)    # Main fucntion will run

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))