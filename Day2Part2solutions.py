# Advent of Code 2024 - Day 2 Part Two
# Reads puzzle input from input.txt

import bisect

def solve():
    with open(r"E:\advent\input.txt") as f:
        puzzle_input = f.read().strip()

    # parse ranges
    ranges = []
    for part in puzzle_input.split(","):
        a, b = map(int, part.split("-", 1))
        if a > b:
            a, b = b, a
        ranges.append((a, b))

    max_b = max(b for (_, b) in ranges)
    max_digits = len(str(max_b))

    repeated = set()

    # Generate digit‐block repeated m >= 2 times
    for d in range(1, max_digits + 1):      # block length
        s_min = 10**(d-1)
        s_max = 10**d - 1
        m = 2
        while d * m <= max_digits:          # repeat count
            pow_dm = 10 ** (d * m)
            pow_d  = 10 ** d
            factor = (pow_dm - 1) // (pow_d - 1)

            for s in range(s_min, s_max + 1):
                num = s * factor
                if num > max_b:
                    break
                repeated.add(num)
            m += 1

    repeated_list = sorted(repeated)

    total = 0
    for a, b in ranges:
        lo = bisect.bisect_left(repeated_list, a)
        hi = bisect.bisect_right(repeated_list, b)
        total += sum(repeated_list[lo:hi])

    print(total)

if __name__ == "__main__":
    solve()
