import sys
data = sys.stdin.read().splitlines()
if not data:
    print(0)
n, m = map(int, data[0].split())
grid = data[1:1 + n]

visited = [[False] * m for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
counter = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#' and not visited[i][j]:
            counter += 1
            stack = [(i, j)]
            visited[i][j] = True
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '#' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

print(counter)


"""
8 6
......
...##.
...##.
......
.###..
.###..
.###..
......
"""

"""
2 1
.
.
"""