'''Date - 10-06-2021
Author - Prajwal Ghadi
Aim - Find the size of a Set in Python.
                and
    Python – Maximum and Minimum in a Set
                and
    Removing Items from the set'''

if __name__ == '__main__':
    a = {1, 2, 34, 3, 1}

    # Finding the Size of Set in python
    print(a)
    print(len(a))


    # Finding Maximum and Minimum values
    print(f'Maximum value from set is {max(a)}')
    print(f'Minimum value from set is {min(a)}')


    # Remove Items from set
    a.remove(34)
    print(a)