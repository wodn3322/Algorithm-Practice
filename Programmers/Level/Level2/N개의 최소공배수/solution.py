import math


def solution(arr):
    answer = 1

    for a in arr:
        answer = answer * a // math.gcd(answer, a)

    return answer


if __name__ == '__main__':
    numArray = [2,6,8,14]
    solution(numArray)
