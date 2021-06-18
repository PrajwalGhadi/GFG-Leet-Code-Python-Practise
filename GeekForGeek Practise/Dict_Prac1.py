'''Date - 10-06-2021
Author - Prajwal Ghadi
Aim - Python | Sort Python Dictionaries by Key or Value.
                    and
    Handling missing keys in Python dictionaries
                    and
    Finding the Size of Dictionary'''

if __name__ == '__main__':

    a = {4:'Prajwal', 1:'Rohit', 3:'Takshak', 2:'Pratik'}

    # Sorting Python Dictionaries
    for i in sorted(a):
        print((i, a[i]), '\n', end='')

    # Handling Missing Keys
    b = a.get(6, 'Not Found')
    print(b)

    # Size of Dictionary
    print(len(a))
