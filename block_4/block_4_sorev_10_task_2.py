import sys

data = sys.stdin.read().splitlines()
if not data:
    print("Empty")

first = data[0].strip()
parts = first.split()

n = int(parts[0])
m = int(parts[1])
k = int(parts[2])

docs = ["" for _ in range(n)]
current = 0
clipboard = ""

for i in range(1, min(m, len(data) - 1) + 1):
    cmd = data[i].strip()
    if cmd == "Next":
        current = (current + 1) % n
    elif cmd == "Backspace":
        if docs[current]:
            docs[current] = docs[current][:-1]
    elif cmd == "Copy":
        doc = docs[current]
        if len(doc) <= k:
            clipboard = doc
        else:
            clipboard = doc[-k:]
    elif cmd == "Paste":
        if clipboard:
            docs[current] += clipboard
    else:
        if len(cmd) == 1 and cmd.islower():
            docs[current] += cmd

result = docs[current]
if len(result) > k:
    result = result[-k:]

if result == "":
    print("Empty")
else:
    print(result)