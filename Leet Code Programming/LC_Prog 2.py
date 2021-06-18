'''Date - 17-06-2021
 Author - Prajwal Ghadi
Aim - Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''

if __name__ == '__main__':

    l1 = list(map(str, input().strip().split()))
    l2 = list(map(str, input().strip().split()))
    ## Reversing of list
    l1.reverse()
    l2.reverse()

    # Separter to separate the string and join it
    seprater = ''
    list1 = seprater.join(l1)
    list2 = seprater.join(l2)

    ## Addition of two string values by converting into integer
    answer = int(list1) + int(list2)

    list3 = []
    # a = ','
    # list3.append(a.join(str(answer)))

    ## Loop to interate the answer by coverting it to string and appending to list by again converting it into integer
    for i in str(answer):
        list3.append(int(i))

    ## Printing the Data on Output window
    print('Original Answer',list3)
    list3.reverse()
    print('Reversed Answer',list3)

    print('Explaination:', seprater.join(l1), '+', seprater.join(l2), '=', answer)
