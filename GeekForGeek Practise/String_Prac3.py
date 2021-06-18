'''Date - 10-06-2021
Author - Prajwal Ghadi
Aim - Python program to print even length words in a string.'''

if __name__ == '__main__':
    a = list( map(str, input().strip().split()))
    print(a)
    nlist = []
    for i in a:
        if len(i) % 2 == 0:
            nlist.append(i)

    if len(nlist) == 0:
        print("Sorry You Enter Strings have Odd Length of Words")
    else:
        for i in nlist:
            print(f"{i} is having Even length")


