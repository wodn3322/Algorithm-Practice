from collections import deque

def solution(s):
    answer = 0
    bracketDeque = deque(list(s))

    for _ in range(len(bracketDeque)):
        checkLoop = True
        checkList = ['[', '{', '(']
        bracketList = []

        for b in bracketDeque:
            if b in checkList:
                bracketList.append(b)
                continue
            else:
                if len(bracketList) == 0:
                    checkLoop = False
                    break
                if (bracketList[-1] == '[' and b == ']') or (bracketList[-1] == '{' and b == '}') or (bracketList[-1] == '(' and b == ')'):
                    bracketList.pop()
                else:
                    checkLoop=False
                    break

        if checkLoop and len(bracketList)==0:
            answer += 1
        bracketDeque.rotate(-1)
    print(answer)
    return answer


if __name__ == '__main__':
    bracket = "[](){}"
    solution(bracket)
