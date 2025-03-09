'''
Homework9
Name: Jai Outland
github link:https://github.com/jaioutland/PYTHON/blob/main/bubble_sort_hw9.py
'''

def bubble_sort(lst):
    # Sort a list using the bubble sort function
    n = len(lst)
    for i in range(n):
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst  # Return the sorted list

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('bubble_sort_doctest.py'))