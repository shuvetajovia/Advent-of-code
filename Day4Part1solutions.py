grid = [list(line.rstrip()) for line in open(r"E:\advent\input.txt")]

R = len(grid)
C = len(grid[0])
cnt = 0

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1),
]

for r in range(R):
    for c in range(C):
        if grid[r][c] != '@':
            continue
        neighbors = 0
        for dr, dc in dirs:
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C:
                if grid[rr][cc] == '@':
                    neighbors += 1
        if neighbors < 4:
            cnt += 1

print(cnt)
