'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Python program to count Even and Odd numbers in a List.'''

if __name__ == '__main__':

    a = list(map(int, input().strip().split()))

    e = list(filter(lambda x: (x%2 == 0), a))
    o = list(filter(lambda x: (x%2 != 0), a))

    print(f'{len(e)} Even Numbers \n{len(o)} Odd Number')