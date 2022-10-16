def solution(clothes):
    answer = 1

    clothDict ={}

    for cloth in clothes:
        if cloth[1] in clothDict:
            clothDict[cloth[1]].append(cloth[0])
        else:
            clothDict[cloth[1]]=[cloth[0]]

    for c in clothDict:
        answer*=(len(clothDict[c])+1)
    answer-=1

    return answer


if __name__ == '__main__':
    clothList = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    solution(clothList)
