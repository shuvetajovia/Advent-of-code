total = 0
with open(r"E:\advent\input.txt") as f:
    for line in f:
        s = line.strip()
        if len(s) < 2: 
            continue
        max_left = int(s[0])
        best = 0
        for ch in s[1:]:
            d = int(ch)
            best = max(best, 10*max_left + d)
            if d > max_left:
                max_left = d
        total += best
print(total) 
