'''
multi_level_list_hw11
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/blob/main/multi_level_list_hw11.py
'''

def count_zeros(lst):
    # Counts the zeros in a 2D array
    return sum(1 for row in lst for num in row if num == 0)

def replace_with_zero(lst):
    # Replaces negative numbers with zero in a 2D array
    new_lst = []
    for row in lst:
        new_lst.append([0 if num < 0 else num for num in row])
    return new_lst
         

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('multi_level_list_doctest.py'))
