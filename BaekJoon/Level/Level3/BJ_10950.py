def solution():
    loop = int(input())
    answerList =[]
    for i in range(loop):
        a,b=map(int,input().split(" "))
        answerList.append(a+b)

    for i in range(loop):
        print(answerList[i])
    return


if __name__ == '__main__':
    solution()
