import sys


def solution(s):
    answer = []
    zeroCount = 0
    converseCount = 0

    while s != '1':
        zeroCount += s.count('0')
        s = s.replace('0', '')
        sLen = len(s)
        temp = ''
        while sLen != 1:
            rest = sLen % 2
            sLen //= 2
            temp = str(rest) + temp
        s = '1' + temp
        converseCount += 1

    answer.append(converseCount)
    answer.append(zeroCount)
    # print(answer)
    return answer


if __name__ == '__main__':
    num = '110010101001'
    solution(num)
