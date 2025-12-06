ranges = []
with open(r"E:\advent\input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        a, b = map(int, line.split('-'))
        ranges.append((a, b))

# Sort by starting point
ranges.sort()

# Merge intervals
merged = []
start, end = ranges[0]

for a, b in ranges[1:]:
    if a <= end + 1:      # overlapping or touching
        end = max(end, b)
    else:
        merged.append((start, end))
        start, end = a, b

merged.append((start, end))

# Count total IDs covered by merged ranges
total = 0
for a, b in merged:
    total += (b - a + 1)

print(total) 
