def merge_the_tools(string, k):
    n = len(string)
    for i in range(0,n,k):
        substring = string[i:i+k]
        # print(substring)
        substring = remove_duplicate(substring)
        print(substring)

def remove_duplicate(string):
    s = ""
    for i in range(len(string)):
        if string[i] not in s:
            s += string[i]
    return s

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)