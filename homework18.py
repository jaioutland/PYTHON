'''
Homework18
Name: Jai Outland
github link:
'''

def iterate_dictionary(lst): # Repeats through a list to check if each number exists
    dict = {1:"one",2:"two",3:"three"}
    for num in lst:
        try:
            print(dict[num])
        except KeyError:
            print("Number not in dictionary")
    return

def check_if_positive(lst): # Repeats through a list to check if each number exists
    for num in lst:
        try:
            if num < 0:
                raise ValueError("not positive")
            print(num)
        except ValueError as e:
            print(e)
    return

def division(lst): # Repeats through a list to check if each number exists
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