"""
Дана строка s, состоящая из трёх типов скобок: круглых ( ), квадратных [ ] и фигурных { }. Нужно определить, существует ли такой циклический сдвиг этой строки, который является правильной скобочной последовательностью (ПСП).

"""

s = input().strip()
n = len(s)

match = {')': '(', ']': '[', '}': '{'}
found = False

if n == 0:
    print("YES")
    found = True
elif n % 2 != 0:
    print("NO")
    found = True

if not found:
    for i in range(n):
        shifted = s[i:] + s[:i]
        stack = []
        ok = True
        for ch in shifted:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != match[ch]:
                    ok = False
                    break
                stack.pop()
        if ok and not stack:
            print("YES")
            found = True
            break

if not found:
    print("NO")
