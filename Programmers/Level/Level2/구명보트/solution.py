def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people) - 1

    while True:
        if start > end:
            break

        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1

    return answer


if __name__ == '__main__':
    peopleList = [70, 80, 50]
    limitSize = 100
    solution(peopleList, limitSize)
