import sys

def solution(s):
    answer =''
    stringList = s.split(' ')
    print(s)
    for i in range(len(stringList)):
        if i != len(stringList) - 1 :
            answer += stringList[i].capitalize() + ' '
        else:
            answer += stringList[i].capitalize()
    return answer


if __name__ == '__main__':
    num ='3people unFollowed me'
    solution(num)
