import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    # your code goes here
    L = []
    for i in range(size):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
      

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)