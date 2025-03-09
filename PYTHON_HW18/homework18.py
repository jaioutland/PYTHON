'''
Homework18
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/homework18.py
'''

def iterate_dictionary(lst): # Checks if each number exists in dictionary
    dict = {1:"one",2:"two",3:"three"}
    for num in lst:
        try:
            print(dict[num])
        except KeyError:
            print("Number not in dictionary")
    return

def check_if_positive(lst): # Checks if numbers are positive
    for num in lst:
        try:
            if num < 0:
                raise ValueError("not positive")
            print(num)
        except ValueError as e:
            print(e)
    return

def division(lst): # Divides each number by 100
    for num in lst:
        try:
            result = round (100 / num, 2)
            print(result)
        except ZeroDivisionError:
            print("can't divide by zero")    
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest18.py'))