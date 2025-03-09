'''
Homework5
Name:
github link:
'''

def collatz_conjecture(num):
    while num != 1:
        print(float(num))
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    print(float(num))            
     

def add_numbers(num):
    total = 0
    i = 1 
    while i <= num:
        total += i
        i += 1 
    print("sum", total)    





if __name__ == "__main__":
    collatz_conjecture(18.0)
    # import doctest
    # print(doctest.testfile('doctest5.py'))