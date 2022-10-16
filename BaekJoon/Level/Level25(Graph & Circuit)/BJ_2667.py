import sys

count = 0

def solution():
    global count
    lineNum = int(sys.stdin.readline().strip())
    graph = []
    visited = [[0] * lineNum for _ in range(lineNum)]
    answer = []

    for _ in range(lineNum):
        graph.append(list(map(int, list(sys.stdin.readline().strip()))))

    def DFS(x, y):
        global count
        visited[x][y]=1
        count+=1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < lineNum and 0 <= ny < lineNum :
                if visited[nx][ny] == 0 and graph[nx][ny]==1:
                    DFS(nx, ny)
                else:
                    continue


    for i in range(lineNum):
        for j in range(lineNum):
            if graph[i][j]==1 and visited[i][j]==0:
                DFS(i, j)
                answer.append(count)
                count =0
    answer.sort()
    sys.stdout.write(str(len(answer))+'\n')
    for a in answer:
        sys.stdout.write(str(a) + '\n')

    return


if __name__ == '__main__':
    solution()
