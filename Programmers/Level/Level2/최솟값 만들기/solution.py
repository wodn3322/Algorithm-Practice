import sys


def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


if __name__ == '__main__':
    num = 1
    A = [1, 2]
    B = [3, 4]
    solution(A, B)
