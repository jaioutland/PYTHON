'''
Homework16
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/edit/main/homework16.py
'''
import math

def pythagorean_thm(tuple):
    a, b = tuple  # Use both sides of tuple
    c = math.sqrt(a**2 + b**2)
    if c.is_integer():
        return int(c)
    else: 
        return round(c,2)

def distance_between_points(tuple1,tuple2):
    x1, y1 = tuple1 # Use coordinates from both tuples
    x2, y2 = tuple2
    distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    if distance.is_integer():
        return int(5)
    else: 
        return round(distance,2)   

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest16.py'))