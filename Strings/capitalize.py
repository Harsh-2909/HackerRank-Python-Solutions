# s = input().split()
# s = [word[0].upper()+word[1:] for word in s]
# s = " ".join(s)
# print(s)

s = input()
s = " "+s
s = list(s)
for i in range(len(s)):
    if s[i] == ' ':
        s[i+1] = s[i+1].upper()
s = "".join(s[1:])
print(s)