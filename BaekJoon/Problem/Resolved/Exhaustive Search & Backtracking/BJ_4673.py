import sys

def solution():

    num =1
    numList = [i for i in range(1,10001)]

    while 10000>=num:
        nList = list(map(int,list(str(num))))
        nList.append(num)
        if sum(nList) in numList:
            numList.remove(sum(nList))
        num+=1

    for n in numList:
        sys.stdout.write(str(n)+'\n')

    return


if __name__ == '__main__':
    solution()
