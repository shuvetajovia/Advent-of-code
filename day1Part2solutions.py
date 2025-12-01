def solve():
    # Change path if required
    with open(r"E:\advent\input.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    pos = 50  # starting position
    count_zero = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == "L":
            delta = -1
        else:
            delta = 1

        # Simulate every click
        for _ in range(steps):
            pos = (pos + delta) % 100
            if pos == 0:
                count_zero += 1

    print("Password (Part 2):", count_zero)


if __name__ == "__main__":
    solve()
