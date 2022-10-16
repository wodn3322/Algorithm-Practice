def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            mulNum = 0
            for k in range(len(arr1[0])):
                mulNum += arr1[i][k] * arr2[k][j]
            answer[i][j] = mulNum

    return answer


if __name__ == '__main__':
    ar1 = [[1, 4], [3, 2], [4, 1]]
    ar2 = [[3, 3], [3, 3]]
    solution(ar1, ar2)
