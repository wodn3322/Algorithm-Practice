import sys

def solution(s):
    answer =''
    numList = list(map(int,s.split(' ')))
    answer = f'{min(numList)} {max(numList)}'
    return answer


if __name__ == '__main__':
    num ='1'
    solution(s)
