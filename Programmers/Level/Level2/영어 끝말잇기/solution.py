def solution(n, words):
    answer = []

    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] and i != 0:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break

        if words[i] in words[:i]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
    if len(answer) == 0:
        answer.append(0)
        answer.append(0)
    print(answer)
    return answer


if __name__ == '__main__':
    num = 3
    wordList = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    # num =5
    # wordList = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer",
    #             "reference", "estimate", "executive"]
    solution(num, wordList)
