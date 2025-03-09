'''
Homework14
Name: Jai Outland
github link:https://github.com/jaioutland/PYTHON/blob/main/homework14.py
'''
# Global Conversion Constants
lbs_to_kg = 0.453592
inches_to_meters = 0.0254

def convert_to_kg(lbs):
    # Convert pounds to kilograms
    return round(lbs * lbs_to_kg,2)

def convert_to_meters(inches):
    # Convert inches to meters
    return round(inches * inches_to_meters,2)

def bmi_calculation(lbs,height):
    # Calculate BMI
    weight_kg = convert_to_kg(lbs)
    height_m = convert_to_meters(height)
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return 'underweight'
    elif 18.5 <= bmi < 24.9:
        return 'normal weight'
    else:
        return 'obese'

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest14.py'))