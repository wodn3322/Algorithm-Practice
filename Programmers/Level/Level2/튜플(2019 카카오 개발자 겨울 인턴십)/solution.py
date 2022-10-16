def solution(s):
    answer = []

    s = s[1:-1]
    tupleList = []
    temp = []
    textList = ['{', ',', '}']
    num = ''
    for i in s:
        if i in textList:
            if i == '}':
                if int(num) not in temp and num != '':
                    temp.append(int(num))
                    num = ''
                tupleList.append(temp)
                temp = []
            if i == ','and num !='':
                temp.append(int(num))
                num = ''
        else:
            num += i

    length = 1
    while len(tupleList) != 0:
        for tuple in tupleList:
            if len(tuple) == length:
                for t in tuple:
                    if t not in answer:
                        answer.append(t)
                length += 1
                tupleList.remove(tuple)
    return answer


if __name__ == '__main__':
    tupleString = "{{123}}"
    solution(tupleString)
