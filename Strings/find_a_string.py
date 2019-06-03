def count_substring(string, sub_string):
    n = len(string)
    count = 0
    n1 = len(sub_string)
    for i in range(n):
        if string[i:i+n1] == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)