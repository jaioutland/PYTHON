'''
Homework5
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/edit/main/While%20-%20Collatz%20Conjecture.py#L4C12
'''

def collatz_conjecture(num):
    while num != 1:
        print(float(num))  # Print number as a float
        if num % 2 == 0:
            num /= 2       # Divide by 2 if the number is even
        else:
            num = num * 3 + 1   # If odd, multiply by 3 and add 1
    print(float(num))      # Print 1.0 as the final value

def add_numbers(num):
    total = 0
    i = 1 
    while i <= num:
        total += i
        i += 1 
    print("sum", total)    # Print the total sum



if __name__ == "__main__":
    collatz_conjecture(18.0)
    # import doctest
    # print(doctest.testfile('doctest5.py'))