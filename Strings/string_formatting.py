def octal(n):
    s = ""
    while n>0:
        r = n%8
        s = str(r) + s
        n= n//8
    return s

def binary(n):
    s = ""
    while n>0:
        r = n%2
        s = str(r) + s
        n=n//2
    return s

def hexa(n):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    s = ""
    while n>0:
        r = n%16
        if r<10:
            s = str(r) + s
        else:
            s = dic[r] + s
        n=n//16
    return s

def print_formatted(number):
    # your code goes here
    width = len(str(binary(number)))
    for i in range(1, number+1):
        print((str(i).rjust(width))+(octal(i).rjust(width+1))+(hexa(i).rjust(width+1))+(binary(i).rjust(width+1)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# OR
# n = int(input())
# width = len("{0:b}".format(n))
# for i in range(1,n+1):
#   print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)