from collections import deque

grid = [list(line.rstrip()) for line in open(r"E:\advent\input.txt")]
R, C = len(grid), len(grid[0])
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# neighbor @ counts
ncount = [[0]*C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if grid[r][c] == '@':
            s = 0
            for dr,dc in dirs:
                rr,cc = r+dr,c+dc
                if 0<=rr<R and 0<=cc<C and grid[rr][cc]=='@':
                    s += 1
            ncount[r][c] = s

q = deque()
for r in range(R):
    for c in range(C):
        if grid[r][c]=='@' and ncount[r][c] < 4:
            q.append((r,c))

removed = 0
while q:
    r,c = q.popleft()
    if grid[r][c] != '@': 
        continue
    grid[r][c] = '.'   # removed
    removed += 1
    for dr,dc in dirs:
        rr,cc = r+dr,c+dc
        if 0<=rr<R and 0<=cc<C and grid[rr][cc]=='@':
            ncount[rr][cc] -= 1
            if ncount[rr][cc] < 4:
                q.append((rr,cc))

print(removed)
