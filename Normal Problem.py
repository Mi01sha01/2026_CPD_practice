def solve(a):
    b = ""
    for i in range(len(a) - 1, -1, -1):
        if a[i] == "q":
            b += "p"
        elif a[i] == "p":
            b += "q"
        else:
            b += a[i]
    return b


t = int(input())
for _ in range(t):
    a = input()
    print(solve(a))
