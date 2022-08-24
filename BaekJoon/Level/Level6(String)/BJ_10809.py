def solution():
    inputString = input()
    for i in range(ord('z')-ord('a')+1):
        target = chr(ord('a')+i)
        if target in inputString:
            index = inputString.index(chr(ord('a')+i))
            print(index,end=' ')
        else:
            print(-1,end=' ')

    return


if __name__ == '__main__':
    solution()
