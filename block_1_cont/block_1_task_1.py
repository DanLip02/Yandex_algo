"""

"""
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            if j + 1 < m and field[i][j + 1] == '.':
                count += 1

            if i + 1 < n and field[i + 1][j] == '.':
                count += 1
print(count)


