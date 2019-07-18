n, m = map(int, input().split())
l = list(input().split())
A = set(input().split())
B = set(input().split())

print(sum((i in A) - (i in B) for i in l))
