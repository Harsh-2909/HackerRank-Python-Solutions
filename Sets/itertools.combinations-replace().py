from itertools import combinations
s, k = input().split()
k = int(k)
s = sorted(s)
for i in range(1,k+1):
    for j in list(combinations(s,i)):
        print(''.join(list(j)))