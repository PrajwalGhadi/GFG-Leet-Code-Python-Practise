'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Lambda with if but without else in Python.'''

def fibonacci(n):
    fnum = 0
    ranger = n
    snum = 1
    counter = 0
    while counter < ranger:
        print(snum)
        nth = fnum + snum
        fnum = snum
        snum = nth
        counter += 1

if __name__ == '__main__':

    n = int(input())
    fibonacci(n)