'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Program to print the diamond shape.'''

def Diamond(n):

    N = n
    k = 2*N + 1
    for i in range(N):
        for j in range(0, k):

            k -= 1
        for j in range(0, i + 1):
            print("*", end='')
        print('\r')

if __name__ == '__main__':

    n = int(input())
    Diamond(n)