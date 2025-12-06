fresh_ranges = []
ids = []
reading_ranges = True

with open(r"E:\advent\input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            reading_ranges = False
            continue

        if reading_ranges:
            a, b = map(int, line.split("-"))
            fresh_ranges.append((a, b))
        else:
            ids.append(int(line))

count_fresh = 0

for x in ids:
    for a, b in fresh_ranges:
        if a <= x <= b:
            count_fresh += 1
            break

print(count_fresh)
