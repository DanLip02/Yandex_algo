import sys

input_data = sys.stdin.read().strip().split()
idx = 0
cases = int(input_data[idx])
idx += 1

if cases < 0:
    print(-2)

results = []
for _ in range(cases):
    n = int(input_data[idx]);
    idx += 1
    d = int(input_data[idx]);
    idx += 1

    t = [0] * (n + 1)
    k = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i] = int(input_data[idx]);
        idx += 1
        k[i] = int(input_data[idx]);
        idx += 1

    old_wait = [0] * (n + 2)  # old_wait[1] = 0
    for i in range(2, n + 1):
        old_wait[i] = old_wait[i - 1] + k[i - 1]

    extra = [0] * (n + 2)
    for i in range(1, n + 1):
        extra[i] = t[i] - old_wait[i]

    suffix_min = [float('inf')] * (n + 3)
    for i in range(n, 0, -1):
        suffix_min[i] = min(extra[i], suffix_min[i + 1])

    pos = n + 1
    for p in range(1, n + 1):
        if d <= suffix_min[p]:
            pos = p
            break

    results.append(str(pos))

print("\n".join(results))