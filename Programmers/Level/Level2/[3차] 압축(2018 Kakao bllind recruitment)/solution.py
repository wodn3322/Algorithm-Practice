def solution(msg):
    answer = []
    newWord = []
    now = ''
    index = 0
    while index < len(msg):
        now += msg[index]
        if len(now) == 1 or now in newWord:
            index += 1
            continue
        else:
            newWord.append(now)
            if len(now) == 2:
                answer.append(ord(now[0]) - ord('A') + 1)
            else:
                answer.append(26 + newWord.index(now[:-1]) + 1)
            now = ''

    if now != '':
        if now in newWord:
            answer.append(26 + newWord.index(now) + 1)
        else:
            answer.append(ord(now[0]) - ord('A') + 1)

    return answer


if __name__ == '__main__':
    s = 'ABABABABABABABAB'
    solution(s)
