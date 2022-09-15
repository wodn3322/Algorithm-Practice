import sys

def solution(s):
    answer =True
    openBracket =0
    sList = list(s)

    for b in sList:
        if b =='(':
            openBracket+=1
        else:
            if openBracket>0:
                openBracket-=1
            else:
                answer=False
                break
    if openBracket!=0:
        answer =False
    print(answer)
    return answer


if __name__ == '__main__':
    s =')()('
    solution(s)
