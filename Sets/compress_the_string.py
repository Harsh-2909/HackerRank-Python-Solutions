s = input()
count = 1
copy = s[0]
for i in range(1,len(s)):
    if(copy!=s[i]):
        print(f'({count}, {copy})',end=" ")
        copy = s[i]
        count = 1
    else:
        count+=1
print(f'({count}, {copy})')