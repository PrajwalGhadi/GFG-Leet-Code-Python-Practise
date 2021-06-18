'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Program to print half Diamond star pattern.'''

def Diamond():
    pass

if __name__ == '__main__':

    N= int(input())
    for i in range(N):

        for j in range(0, i + 1):
            print("*", end="")
        print()

        # Loop to print the lower half
        # diamond pattern
    for i in range(1, N):

        for j in range(i, N):
            print("*", end="")
        print()