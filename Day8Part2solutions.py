from itertools import combinations

# load points
pts = []
with open(r"E:\advent\input.txt") as f:
    for line in f:
        line = line.strip()
        if not line: 
            continue
        x,y,z = map(int, line.split(","))
        pts.append((x,y,z))

n = len(pts)
if n < 2:
    raise SystemExit("Not enough points")

# build edges with squared distance
edges = []
for i,j in combinations(range(n), 2):
    x1,y1,z1 = pts[i]
    x2,y2,z2 = pts[j]
    dx,dy,dz = x1-x2, y1-y2, z1-z2
    dist2 = dx*dx + dy*dy + dz*dz
    edges.append((dist2, i, j))

edges.sort(key=lambda e: e[0])

# DSU
parent = list(range(n))
size = [1]*n
components = n

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a,b):
    global components
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    components -= 1
    return True

last_pair = None

for _, i, j in edges:
    if union(i, j):
        last_pair = (i, j)
        if components == 1:
            break

if last_pair is None:
    raise SystemExit("No union performed; points may already be connected.")

i, j = last_pair
print(pts[i][0] * pts[j][0])
