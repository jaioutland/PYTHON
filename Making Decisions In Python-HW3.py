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
print()
print(positive_or_negative(10))
print(positive_or_negative(-3))
print(is_able_to_vote(8))
print(is_able_to_vote(28))
print(can_buy_alcohol(23))
print(can_buy_alcohol(16))
print(senior_discount(72))
print(senior_discount(54))
print(is_able_to_drive(15))
print(is_able_to_drive(18))
print(is_able_to_drive(13))
print(is_able_to_drive(25))
print()
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))
