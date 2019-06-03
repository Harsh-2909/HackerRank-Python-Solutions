if __name__ == '__main__':
    n = int(input())
    students = []
    marks = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])
        marks.append(score)
    marks.sort()
    h1 = marks[0]
    for i in range(1, n):
        if marks[i] != h1:
            h2 = marks[i]
            break
    students.sort()
    for _ in range(n):
        if students[_][1] == h2:
            print(students[_][0])
    