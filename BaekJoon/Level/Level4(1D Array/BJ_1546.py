def solution():
    num  = int(input())
    gradeList = list(map(int,input().split(" ")))
    maxGrade = max(gradeList)
    sum = 0 ;
    for i in gradeList:
        sum += i/maxGrade*100

    print(sum/num)

    return


if __name__ == '__main__':
    solution()
