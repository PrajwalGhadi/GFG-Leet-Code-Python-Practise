'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Programs for printing pyramid patterns in Python.'''

n = int(input())

k = n - 1
for i in range(0, n):
    for j in range(0, i + 1):
        print('*', end='')
    print()
