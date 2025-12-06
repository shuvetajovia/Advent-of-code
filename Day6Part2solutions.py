


from operator import add, mul

# Load and pad lines
with open(r"E:\advent\input.txt") as f:
    lines = [ln.rstrip("\n") for ln in f.readlines()]

R = len(lines)
C = max(len(ln) for ln in lines)
grid = [list(ln.ljust(C)) for ln in lines]

# Identify separator columns
sep = [all(grid[r][c] == " " for r in range(R)) for c in range(C)]

# Extract non-blank intervals
intervals = []
c = 0
while c < C:
    if not sep[c]:
        start = c
        while c < C and not sep[c]:
            c += 1
        intervals.append((start, c))   # [start, c)
    else:
        c += 1


def eval_problem(start, end):
    # Identify operator: bottom-most non-space char in this block
    op = None
    for c in range(start, end):
        ch = grid[R-1][c]
        if ch in "+*":
            op = ch
            break
    if op is None:
        raise ValueError("Operator not found in block.")

    # Read columns right-to-left
    numbers = []
    for c in range(end - 1, start - 1, -1):
        col_digits = [grid[r][c] for r in range(R-1)]  # exclude bottom operator row
        s = "".join(ch for ch in col_digits if ch.isdigit())
        if s:
            numbers.append(int(s))

    # Evaluate
    if op == "+":
        return sum(numbers)
    else:
        p = 1
        for n in numbers:
            p *= n
        return p


# Sum all problems
total = sum(eval_problem(a, b) for a, b in intervals)
print(total)
