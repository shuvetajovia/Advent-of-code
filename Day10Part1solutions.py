# Day 10 – Factory
# Reads from: E:\advent\input.txt

import re
import random

def min_presses(n, cols, target):
    m = len(cols)
    rows = [0]*n
    for j, col in enumerate(cols):
        for i in col:
            rows[i] |= (1 << j)

    aug = [rows[i] | ((target[i] & 1) << m) for i in range(n)]
    piv = [-1] * m
    r = 0

    for c in range(m):
        sel = None
        for i in range(r, n):
            if (aug[i] >> c) & 1:
                sel = i
                break
        if sel is None:
            continue
        aug[r], aug[sel] = aug[sel], aug[r]
        piv[c] = r
        for i in range(n):
            if i != r and ((aug[i] >> c) & 1):
                aug[i] ^= aug[r]
        r += 1
        if r == n:
            break

    for i in range(r, n):
        if (aug[i] & ((1 << m) - 1)) == 0 and ((aug[i] >> m) & 1):
            return None

    part = 0
    for c in range(m):
        if piv[c] != -1:
            if (aug[piv[c]] >> m) & 1:
                part |= (1 << c)

    basis = []
    free_vars = []
    for c in range(m):
        if piv[c] == -1:
            vec = 1 << c
            for pc in range(m):
                if piv[pc] != -1:
                    if (aug[piv[pc]] >> c) & 1:
                        vec |= (1 << pc)
            basis.append(vec)
            free_vars.append(c)

    k = len(basis)
    if k == 0:
        return part.bit_count()

    if k > 26:
        best = part.bit_count()
        for _ in range(200000):
            mask = random.getrandbits(k)
            vec = part
            for i in range(k):
                if (mask >> i) & 1:
                    vec ^= basis[i]
            bc = vec.bit_count()
            if bc < best:
                best = bc
        return best

    best = None
    for mask in range(1 << k):
        vec = part
        for i in range(k):
            if (mask >> i) & 1:
                vec ^= basis[i]
        bc = vec.bit_count()
        if best is None or bc < best:
            best = bc

    return best


# -----------------------------
#     READ FROM YOUR FILE
# -----------------------------

with open(r"E:\advent\input.txt") as f:
    lines = f.read().strip().splitlines()

total = 0

for line in lines:
    if not line.strip():
        continue

    lights = re.search(r"\[([.#]+)\]", line).group(1)
    target = [1 if c == "#" else 0 for c in lights]
    n = len(target)

    cols = []
    groups = re.findall(r"\((.*?)\)", line)
    for g in groups:
        if g.strip() == "":
            cols.append([])
        else:
            cols.append([int(x) for x in g.split(",")])

    ans = min_presses(n, cols, target)
    total += ans

print(total)
