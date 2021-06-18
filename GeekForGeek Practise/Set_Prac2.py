'''Date - 10-06-2021
Author - Prajwal Ghadi
Aim - Python – Check if two lists have at least one element common.'''

if __name__ == '__main__':
    a = [1, 2, 3, 5, 6, 45]
    b = [ 7, 45, 5, 77, 33]
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)

    print(f'{c} are the common numbers')
