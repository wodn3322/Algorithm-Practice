import sys


def solution():
    meetingNum = int(sys.stdin.readline().strip())
    meetingList = []

    for _ in range(meetingNum):
        meetingList.append(list(map(int, sys.stdin.readline().strip().split())))

    # lambda 생각하기
    meetingList = sorted(meetingList, key=lambda x: (x[1], x[0]))
    meetingCount = 1
    endTime = meetingList[0][1]
    for i in range(1, meetingNum):
        if meetingList[i][0] >= endTime:
            endTime = meetingList[i][1]
            meetingCount += 1

    sys.stdout.write(str(meetingCount) + '\n')

    return


if __name__ == '__main__':
    solution()
