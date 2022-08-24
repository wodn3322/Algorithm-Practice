def solution():
    caseNum = int(input())
    inputList = []

    for i in range(caseNum):
        inputList.append(list(input().split()))

    for i in range(caseNum):
        answer = ""
        for j in range(len(inputList[i][1])):
            answer += inputList[i][1][j] * int(inputList[i][0])
        print(answer)

    return


if __name__ == '__main__':
    solution()
