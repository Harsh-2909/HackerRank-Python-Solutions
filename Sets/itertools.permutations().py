from itertools import permutations
s, k = input().split()
k = int(k)
s = sorted(s)
for i in list(permutations(s, k)):
    print(''.join(list(i)))
