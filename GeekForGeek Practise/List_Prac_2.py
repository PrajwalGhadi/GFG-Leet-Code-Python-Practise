'''Date - 10-06-2021
Author - Prajwal Ghadi
Aim - Python program to swap two elements in a list.'''

def swap(l, fnum, snum):
    listt = l
    fnum = fnum
    snum = snum

    listt[fnum], listt[snum] = listt[snum],listt[fnum]
    print(listt)

l = list(map(int, input().strip().split()))
f = list(map(int, input('Which 2 positions you want to swap:').strip().split()))
fnum = f[0]
snum = f[1]
swap(l, fnum, snum)
