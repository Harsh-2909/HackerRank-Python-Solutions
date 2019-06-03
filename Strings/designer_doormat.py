# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

for i in range((N//2)):
    print((".|."*i).rjust((M-3)//2,'-')+".|."+(".|."*i).ljust((M-3)//2,'-'))
print(''.rjust((M-7)//2,'-')+"WELCOME"+''.ljust((M-7)//2,'-'))
for i in range((N//2)-1, -1, -1):
    print((".|."*i).rjust((M-3)//2,'-')+".|."+(".|."*i).ljust((M-3)//2,'-'))