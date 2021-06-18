'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Python program to build Armstrong number.'''


if __name__ == '__main__':

    n = str(int(input()))
    listt = []
    for i in n:
        a = int(i) ** 3
        listt.append(a)

    print(listt)
    total = 0
    for i in range(0, len(listt)):
        total = total + listt[i]


    if total == int(n):
        print(f'{n} is an Armstrong')
    else:
        print(f'{n} is not an Armstrong')


