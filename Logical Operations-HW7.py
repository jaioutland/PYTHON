'''
Homework7
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/Logical%20Operations-HW7.py
'''

def fizzbuzz(num):
    # Print numbers from 1 to n
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("Buzz")        
        else:
            print(i)    

def scholarship_eligibility(gpa,credits):
    # Check if student is eligible for scholarship based on GPA and total credits
    gpa = float(input("Enter your GPA"))
    credits = int(input("Enter your total credits:"))

    eligible = gpa > 3.5 and credits > 60

    print("Eligible for scholarship", eligible)

def max_of_three_numbers(num1,num2,num3):
    # Find the largest number among the three inputs
    num1 = (int(input("First number: ")))
    num2 = (int(input("Second number: ")))
    num3 - (int(input("Third number: ")))
    print("The largest number is:", max_num)




if __name__ == "__main__":
    fizzbuzz(15)
    scholarship_eligibility(3.8, 75)
    max_of_three_numbers(5,8,3)
    import doctest
    print(doctest.testfile('doctest7.py'))