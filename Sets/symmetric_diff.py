m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

m_set, n_set = list(m_set - n_set), list(n_set - m_set)
l = [*m_set, *n_set]
l.sort()
for i in l:
    print(i)