'''
Homework4
Name: Jai Outland
github link:
'''
def grade_calculator(score):
    if 0 <= score <= 100: 
         if score >= 90:
            return "A"
    elif score >= 80:
        return "B"
    elif score  >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def even_or_odd(num):  
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(grade_calculator(95))
print(grade_calculator(83))
print(grade_calculator(49))
print(grade_calculator(-5))
print(grade_calculator(102))
print(even_or_odd(5))
print(even_or_odd(2))
 
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))

