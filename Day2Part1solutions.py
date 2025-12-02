# Advent of Code 2024 - Day 2 Part One
# Reads puzzle input from input.txt

from math import ceil

def ceil_div(a, b):
    return (a + b - 1) // b

def solve():
    with open(r"E:\advent\input.txt") as f:
        puzzle_input = f.read().strip()

    # parse ranges
    ranges = []
    for part in puzzle_input.split(","):
        a,b = map(int, part.split("-",1))
        if a > b:
            a,b = b,a
        ranges.append((a,b))

    max_b = max(b for _,b in ranges)
    max_digits = len(str(max_b))

    total = 0

    # For Part 1: only s repeated exactly 2 times
    # number = s * (10^k + 1)
    for k in range(1, max_digits // 2 + 1):      # block length
        factor = 10**k + 1                       # double pattern
        s_min = 10**(k-1)
        s_max = 10**k - 1

        for a, b in ranges:
            # find s such that a ≤ s*factor ≤ b
            s_low = max(s_min, ceil_div(a, factor))
            s_high = min(s_max, b // factor)

            if s_low <= s_high:
                count = s_high - s_low + 1
                total += factor * (count * (s_low + s_high) // 2)

    print(total)

if __name__ == "__main__":
    solve()
