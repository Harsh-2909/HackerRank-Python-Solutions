if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    h1 = arr[0]
    for i in range(1,n):
        if arr[i] != h1:
            print(arr[i])
            break
