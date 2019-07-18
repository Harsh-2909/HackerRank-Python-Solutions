vow = "AEIOU"
def minion_game(string):
    Stuart = 0
    Kevin = 0
    for i in range(len(string)):
        if string[i] in vow:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    if Stuart > Kevin:
        print("Stuart {}".format(Stuart))
    elif Kevin > Stuart:
        print("Kevin {}".format(Kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)