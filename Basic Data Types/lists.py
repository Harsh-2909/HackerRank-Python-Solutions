if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        com = input().split()
        if com[0] == "print":
            print(arr)
        elif len(com) == 3:
            arr.insert(int(com[1]), int(com[2]))
        elif len(com) == 2:
            str = "arr."+com[0]+"("+com[1]+")"
            eval(str)
        elif len(com) == 1:
            str = "arr."+com[0]+"()"
            eval(str)
