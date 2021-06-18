'''Date - 17-06-2021
 Author - Prajwal Ghadi
Aim - Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''

if __name__ == '__main__':

    l1 = list(map(int, input().strip().split()))
    l2 = list(map(int, input().strip().split()))
    ## Adding or Merging 2 Arrrays or List
    l3 = l1+l2
    ## Printing mean of 2 lists
    print(sum(l3) / len(l3))
    print(f'Explanation: Merged arrray = {l3} and Median is {sum(l3) / len(l3)}')
