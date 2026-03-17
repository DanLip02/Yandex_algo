import sys
from collections import defaultdict

n, m = map(int, input().split())
cont_1 = []
points = set()

for _ in range(n):
    l, r, v = map(int, input().split())
    cont_1.append((l, r, v))
    points.update([l, r, r+1])

cont_2 = [int(input()) for _ in range(m)]
points.update(cont_2)
points = sorted(points)
idx = {x: i for i, x in enumerate(points)}
diff = [0] * (len(points) + 1)

for l, r, v in cont_1:


    sign_v = v if l % 2 == 1 else -v
    diff[idx[l]] += sign_v
    diff[idx[r+1]] -= sign_v

for i in range(1, len(points)):
    diff[i] += diff[i-1]

for q in cont_2:
    res = -diff[idx[q]] if q % 2 == 0 else diff[idx[q]]
    print(res)

#input
"""
1 3
9 9 1
8
9
10
"""

#output
"""
0
1
0
"""
