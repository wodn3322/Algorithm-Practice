count = 0


def solution(numbers, target):
    global count
    answer = 0

    def DFS(index, nowSum):
        global count

        if index >= len(numbers):
            if nowSum == target:
                count += 1
            return

        DFS(index + 1, nowSum + numbers[index])
        DFS(index + 1, nowSum - numbers[index])

    DFS(0, 0)
    answer = count

    return answer


if __name__ == '__main__':
    n, t = [1, 1, 1, 1, 1], 3
    solution(n, t)
