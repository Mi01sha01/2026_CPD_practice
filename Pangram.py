def solve(n, s):
    if n < 26 or len(set(s)) < 26:
        return "NO"
    return "YES"


n = int(input())
s = input().upper()
print(solve(n, s))
