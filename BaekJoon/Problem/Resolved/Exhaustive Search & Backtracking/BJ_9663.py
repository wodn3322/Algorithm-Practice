import sys

count = 0

# 시간초과
def solution():
    global count
    n = int(sys.stdin.readline().strip())
    locationList = [-1] * n

    def check(num):
        for i in range(num):
            if locationList[num] == locationList[i] or abs(locationList[num] - locationList[i]) == abs(num - i):
                return False
        return True

    def BruteForce(num):
        global count

        if num == n:
            count += 1
            return

        for i in range(n):
            locationList[num] = i
            if check(num):
                BruteForce(num + 1)

    BruteForce(0)
    sys.stdout.write(str(count) + '\n')

    return


if __name__ == '__main__':
    solution()
