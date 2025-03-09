'''
Homework3
Name: Jai Outland
github link:
'''

def positive_or_negative(num):
    return num >= 0

def is_able_to_drive(age):
    return age >= 16

def is_able_to_vote(age):
    return age >= 18

def can_buy_alcohol(age):   
    return age >= 21

def senior_discount(age):
    return age >= 65

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))