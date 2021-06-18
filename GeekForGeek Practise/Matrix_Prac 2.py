'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Python – Group similar elements into Matrix
Input : test_list = [1, 3, 4, 4, 2, 3]
Output : [[1], [2], [3, 3], [4, 4]]

Input : test_list = [1, 3, 4, 2]
Output : [[1], [2], [3], [4]]'''

if __name__ == '__main__':

    n = [1, 3, 4, 2]
    m = []
    for i in range(len(n)):
        if n[i] == n[i+1]:
            m.append(n[i], n[i+1])
        else:
            print('hhh')

    print(m)