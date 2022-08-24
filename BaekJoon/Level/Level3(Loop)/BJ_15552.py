import sys

def solution():
    loop = int(input())
    answserList =[]
    for i in range(loop):
        a,b = map(int,sys.stdin.readline().rstrip("\n").split(" "))
        answserList.append(a+b)
    for i in range(loop):
        print(answserList[i])
    return


if __name__ == '__main__':
    solution()