'''Date - 15-06-2021 - 16-06-2021
 Author - Prajwal Ghadi
Aim - Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]..'''


def calculate(n, target):
    nlist = n
    nlen = len(nlist)
    target = target
    # i = 0
    a = []
    for i in range(nlen):
        for j in nlist:
            if nlist[i] + j == target:
                a.append(i)
                break
    print(a)

if __name__ == '__main__':
    n = list(map(int, input().strip().split()))
    target = int(input())

    calculate(n, target)

