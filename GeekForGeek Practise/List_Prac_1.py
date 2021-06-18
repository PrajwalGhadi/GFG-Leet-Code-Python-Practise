'''Date - 10-06-2021
Author - Prajwal Ghadi
Aim - Given a list, write a Python program to swap first and last element of the list.'''


n = list(map(int, input().rstrip().rsplit()))
n.remove(n[-1])
n.remove(n[0])

print(n)
