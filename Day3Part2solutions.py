def max_subseq_12(s):
    k = 12
    drop = len(s) - k
    stack = []
    for ch in s:
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)
    return int("".join(stack[:k]))

total = 0
with open(r"E:\advent\input.txt") as f:
    for line in f:
        total += max_subseq_12(line.strip())

print(total)
