import sys

def solution():

    n,m,b = map(int,sys.stdin.readline().strip().split(' '))
    ground =[]
    maxHeight = 0
    minHeight =0

    for _ in range(n):
        data =list(map(int,sys.stdin.readline().strip().split(' ')))
        maxHeight = max(maxHeight,max(data))
        minHeight = min(minHeight,min(data))
        ground.append(data)
    


    return


if __name__ == '__main__':
    solution()
