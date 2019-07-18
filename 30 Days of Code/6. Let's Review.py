t = int(input())
st = []
even = odd = ''

for i  in range(t):
    st.append(input())

for  i in range(t):
    l = len(st[i])
    s = st[i]
    for j in range(l):
        if j % 2 == 0:
            even = even + s[j]
        else:
            odd = odd + s[j]
    print(even + " " + odd)
    even = odd = ''