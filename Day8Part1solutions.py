import math
from itertools import combinations

# ---- Load points ----
pts = []
with open(r"E:\advent\input.txt") as f:
    for line in f:
        if line.strip():
            x, y, z = map(int, line.split(","))
            pts.append((x, y, z))

n = len(pts)

# ---- Build all pairwise distances ----
edges = []
for i, j in combinations(range(n), 2):
    x1, y1, z1 = pts[i]
    x2, y2, z2 = pts[j]
    d = math.dist((x1, y1, z1), (x2, y2, z2))
    edges.append((d, i, j))

# Sort edges by shortest distance
edges.sort(key=lambda x: x[0])

# ---- DSU (Union–Find) ----
parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

# ---- Apply the 1000 shortest edges ----
for _, i, j in edges[:1000]:
    union(i, j)

# ---- Compute circuit sizes ----
circuits = {}
for i in range(n):
    r = find(i)
    circuits[r] = circuits.get(r, 0) + 1

# Find the sizes of all circuits
sizes = sorted(circuits.values(), reverse=True)

# Multiply the largest three
answer = sizes[0] * sizes[1] * sizes[2]
print(answer)
