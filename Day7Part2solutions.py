import sys
sys.setrecursionlimit(10000)

# load grid (pad rows to same width)
with open(r"E:\advent\input.txt") as f:
    lines = [ln.rstrip("\n") for ln in f]
R = len(lines)
C = max((len(ln) for ln in lines), default=0)
grid = [list(ln.ljust(C)) for ln in lines]

# find S
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            sr, sc = r, c
            break
    else:
        continue
    break

# build adjacency function (edges from (r,c) -> list of (r2,c2) ; outside -> terminal)
def out_neighbors(r, c):
    ch = grid[r][c] if 0 <= r < R and 0 <= c < C else " " 
    if ch == "^":
        nbrs = []
        for nc in (c-1, c+1):
            if 0 <= nc < C:
                nbrs.append((r, nc))
            else:
                # off-grid horizontally -> terminal (represented by None)
                nbrs.append(None)
        return nbrs
    else:
        # empty or other -> goes down
        if r+1 < R:
            return [(r+1, c)]
        else:
            return [None]  # goes off bottom -> terminal

from functools import lru_cache

@lru_cache(maxsize=None)
def ways(node):
    # node is (r,c) or None for terminal
    if node is None:
        return 1
    r, c = node
    nbrs = out_neighbors(r, c)
    total = 0
    for nb in nbrs:
        total += ways(nb)
    return total

start = (sr+1, sc)
print(ways(start))
