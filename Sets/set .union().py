n = input()
s1 = set(map(int, input().split()))
b = input()
s2 = set(map(int, input().split()))

print(len(s1.union(s2)))
