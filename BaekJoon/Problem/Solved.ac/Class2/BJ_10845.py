import sys


def solution():
    n = int(sys.stdin.readline().strip())
    queue = []
    answer = []

    for _ in range(n):
        command = sys.stdin.readline().strip().split(' ')
        if command[0] == 'push':
            queue.append(command[1])
        elif command[0] == 'pop':
            if len(queue):
                answer.append(queue[0])
                del queue[0]
            else:
                answer.append(-1)
        elif command[0] == 'size':
            answer.append(len(queue))
        elif command[0] == 'empty':
            if len(queue):
                answer.append(0)
            else:
                answer.append(1)
        elif command[0] == 'front':
            if len(queue):
                answer.append(queue[0])
            else:
                answer.append(-1)
        elif command[0] == 'back':
            if len(queue):
                answer.append(queue[-1])
            else:
                answer.append(-1)

    for a in answer:
        print(a)

    return


if __name__ == '__main__':
    solution()
