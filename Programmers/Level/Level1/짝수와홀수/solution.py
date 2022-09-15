import sys

def solution(num):
    answer =''
    if num %2 ==1:
        answer = 'Odd'
    else:
        answer='Even'

    return answer


if __name__ == '__main__':
    num = 11
    solution(num)
