def grade_calculator(score):
    if 0 <= score <= 100: 
                            # Grade letter assigned based on the score
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

def even_or_odd(num):  # Double check to see if the number is divisble by 2
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
 

