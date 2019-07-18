if __name__ == '__main__':
    s = input()
    flag = [0,0,0,0,0]
    for i in s:
        if i.isalnum() == True:
            flag[0] = 1
        if i.isalpha() == True:
            flag[1] = 1
        if i.isdigit() == True:
            flag[2] = 1
        if i.islower() == True:
            flag[3] = 1
        if i.isupper() == True:
            flag[4] = 1
    for i in flag:
        if i == 1:
            print("True")
        else:
            print("False")