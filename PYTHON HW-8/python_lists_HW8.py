'''
Homework8
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/python_lists_HW8.py
'''

def sum_numbers(lst):
    # Calculate the sum of all numbers
    total = 0        # Starting with 0
    for num in lst:
        total += num # Add each number to the total
    return total     

def largest_number(lst):
    # Find the largest number in a list
    max_num = lst[0]  # Consider first number to be largest number
    for num in lst:
        if num > max_num: 
            max_num = num
    return max_num

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py')) # Run the test script and print results
