from operator import add, mul

# read and pad lines to same width
with open(r"E:\advent\input.txt") as f:
    lines = [ln.rstrip("\n") for ln in f.readlines()]
maxw = max(len(ln) for ln in lines)
grid = [list(ln.ljust(maxw)) for ln in lines]

R, C = len(grid), maxw

# find separator columns (a column is separator if every row has a space there)
sep = [all(grid[r][c] == " " for r in range(R)) for c in range(C)]

# build intervals of non-separator contiguous columns
intervals = []
c = 0
while c < C:
    if not sep[c]:
        start = c
        while c < C and not sep[c]:
            c += 1
        intervals.append((start, c))  # [start, c)
    else:
        c += 1

def eval_problem(start, end):
    # For each row in this column span, join chars and strip.
    parts = []
    for r in range(R):
        s = "".join(grid[r][start:end]).strip()
        if s:
            parts.append(s)
    if not parts:
        return 0
    op = parts[-1]            # last non-empty line is operator (+ or *)
    nums = [int(x) for x in parts[:-1]]  # preceding lines are numbers, top-to-bottom
    if op == "+":
        return sum(nums)
    elif op == "*":
        prod = 1
        for n in nums: prod *= n
        return prod
    else:
        raise ValueError("unknown operator: " + op)

total = sum(eval_problem(a, b) for a, b in intervals)
print(total)
