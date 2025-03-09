'''
operation_lists_hw10
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/operation_lists_hw10.py
'''

def find_missing_number(lst):
    # Find the missing numbers between smallest and largest in a list
    return [num for  num in range(0, max(lst)+ 1) if num not in lst] 

def even_partition(lst):
    # Remove all even numbers from a given list
    return [num for num in lst if num & 1 == 0]

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('operation_lists_doctest.py'))