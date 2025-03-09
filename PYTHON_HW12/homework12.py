'''
Homework12
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/homework12.py
'''

import math

def rectangle (side1, side2):
# Calculate the area of a rectangle
    area = side1 * side2
    return(f'The area of the rectangle is {area} square units')

print('')

def circle (radius):
# Calculate the area of a circle
    area = math.pi * radius ** 2
    return(f'The area of a circle is {area:.2f} square units')
 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest12.py'))
