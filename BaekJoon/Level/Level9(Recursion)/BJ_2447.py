## 너무 모르겠어서 답지 봄...
## 복습 필수

def solution():
    num = int(input())

    def stepStar(n):
        if n == 1:
            return ['*']

        starList = stepStar(n // 3)

        tempList = []

        for i in range(3):
            if i != 1:
                for s in starList:
                    tempList.append(s * 3)
            else:
                for s in starList:
                    tempList.append(s + " " * (n // 3) + s)
        return tempList

    temp = stepStar(num)
    for i in temp:
        print(i)

    return


if __name__ == '__main__':
    solution()

# if n != 3:
#     resultStarList = stepStar(n // 3)
#     return
# else:
#     tempList =[]
#     for i in range(3):
#         if i ==1:
#             for s in star:
#                tempList.append(s+"   "+s)
#         else:
#             for s in star:
#                 tempList.append(s*3)
#     print(tempList)
#     return tempList
