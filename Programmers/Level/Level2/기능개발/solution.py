import math

def solution(progresses, speeds):
    answer = []

    workingDay =[]
    for p , s in zip(progresses,speeds):
        day = math.ceil((100-p)/s)
        workingDay.append(day)
    # print(workingDay)
    functionCont =0
    maxNum =workingDay[0]
    for i in workingDay:
        if i>maxNum:
            maxNum=i
            answer.append(functionCont)
            functionCont=1
        else:
            functionCont+=1
    answer.append(functionCont)
    print(answer)
    return answer


if __name__ == '__main__':
    progressList =[93, 30, 55]
    speedList =[1, 30, 5]
    solution(progressList,speedList)
