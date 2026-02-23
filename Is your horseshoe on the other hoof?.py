colors = list(map(int, input().split()))
diff_colors = len(set(colors))
print(4 - diff_colors)
