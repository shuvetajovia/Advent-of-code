from collections import deque

grid = [list(line.rstrip("\n")) for line in open(r"E:\advent\input.txt")]
R = len(grid); C = max(len(row) for row in grid)
# pad rows
for row in grid:
    if len(row) < C:
        row += [" "] * (C - len(row))

# find S
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            sr, sc = r, c

dirs = None
q = deque()
q.append((sr + 1, sc))   # beam starts one row below S
seen = set()
splits = 0

while q:
    r, c = q.popleft()
    if (r, c) in seen: 
        continue
    if r < 0 or r >= R or c < 0 or c >= C:
        continue
    seen.add((r, c))
    ch = grid[r][c]
    if ch == "^":
        splits += 1
        # emit from immediate left and right (same row)
        if c - 1 >= 0:
            q.append((r, c - 1))
        if c + 1 < C:
            q.append((r, c + 1))
    elif ch == "." or ch == "S" or ch == " ":
        # empty → beam continues downward
        q.append((r + 1, c))
    else:
        # any other char treat as empty (safe)
        q.append((r + 1, c))

print(splits)
