n = int(input())
if n>=1 and n<=100:
    if n%2==1:
        print("Weird")
    elif n%2==0 and (n>=2 and n<=5):
        print("Not Weird")
    elif n%2==0 and (n>=6 and n<=20):
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")
else:
    print("Wrong Input")