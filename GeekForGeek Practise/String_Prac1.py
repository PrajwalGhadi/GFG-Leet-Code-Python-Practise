'''Date - 10-06-2021
Author - Prajwal Ghadi
Aim - Python program to check whether the string is Palindrome.'''

def Palindrome(a):
    stringer = a

    # Now to Calculate the Palindrome we need to take some parameters
    start = 0
    last = len(stringer) - 1
    middle = (len(stringer) - 1) // 2
    flag = 0

    # Loop for calculate the Palindrome

    while start < middle:

        if stringer[start] == stringer[last]:

            start += 1
            last -= 1
        else:
            flag = 1
            break
    if flag == 0:
        print(f'{stringer} is an Palindrome')
    else:
        print(f'{stringer} is Not an Palindrome')


if __name__ == '__main__':

    a = input()
    Palindrome(a)