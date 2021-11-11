# def colordfs(i, j):
#     if (i >= 0 and i <= n + 1 and j >= 0 and j <= m + 1 and g[i][j] == 0):
#         g[i][j] = 2
#         color(i, j - 1)
#         color(i, j + 1)
#         color(i - 1, j)
#         color(i + 1, j)


def colorbfs(i, j):
    q = []
    q.append((i, j))
    while(len(q) > 0):
        e = q.pop(0)
        x = e[0]+1
        y = e[1]
        if x <= n + 1 and x >= 0 and y <= m + 1 and y >= 0 and visited[x][y] == 0 and g[x][y] == 0:
            g[x][y] = 2
            q.append((x, y))
            visited[x][y] = 1
        x = e[0]
        y = e[1]+1
        if x <= n + 1 and x >= 0 and y <= m + 1 and y >= 0 and visited[x][y] == 0 and g[x][y] == 0:
            g[x][y] = 2
            q.append((x, y))
            visited[x][y] = 1
        x = e[0]-1
        y = e[1]
        if x <= n + 1 and x >= 0 and y <= m + 1 and y >= 0 and visited[x][y] == 0 and g[x][y] == 0:
            g[x][y] = 2
            q.append((x, y))
            visited[x][y] = 1
        x = e[0]
        y = e[1]-1
        if x <= n + 1 and x >= 0 and y <= m + 1 and y >= 0 and visited[x][y] == 0 and g[x][y] == 0:
            g[x][y] = 2
            q.append((x, y))
            visited[x][y] = 1


inp = input().split()
n = int(inp[0])
m = int(inp[1])
g = [[0]*(m+2) for i in range(n+2)]
visited = [[0]*(m+2) for i in range(n+2)]
for i in range(n):
    temp = input()
    for j in range(m):
        g[i+1][j+1] = int(temp[j])
total = 0
colorbfs(0, 0)
for i in range(1, n+1):
    for j in range(1, m+1):
        if g[i][j] == 1:
            if g[i][j - 1] == 2:
                total += 1
            if g[i][j + 1] == 2:
                total += 1
            if g[i - 1][j] == 2:
                total += 1
            if g[i + 1][j] == 2:
                total += 1
print(total)
