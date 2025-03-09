'''
Homework6
Name: Jai Outland
github link:
'''

def div_by_seven(num):
    # Print all numbers divisible by 7 from 1 up to num
    for i in range(1, num +1):  
        # Check and see if the number is divisible by 7
        if i % 7 == 0:
            print(i)  # Print if the number is divisible by 7

def squares_of_numbers(num):
    # Loop through numbers from 1 up to num
    for i in range(1, num):
        print(i ** 2)   # Print the square of the number

print("Numbers divisble by 7 up to 30:")
print("\nSquares of numbers up to 5:")


if __name__ == "__main__": # Run test
    import doctest
    print(doctest.testfile('doctest6.py'))