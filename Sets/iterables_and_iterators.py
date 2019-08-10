from itertools import combinations
n = int(input())
s = list(input().split())
k = int(input())
total_count, a_count = 0, 0 
for i in combinations(s,k):
    if 'a' in i:
        a_count+=1
    total_count +=1
print(a_count/total_count)
