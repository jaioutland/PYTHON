'''
Homework15
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/edit/main/homework15.py
'''
def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else: 
        n = n * factorial(n-1)
        
    return n

def main(num1):
    f = factorial(num1)  #6
    print(f'"The factorial of {num1} is {f}."')   #The factorial of 3 is 6

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest15.py'))
