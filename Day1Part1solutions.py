def solve():
    # starting position
    position = 50  
    count_zero = 0

    # read all lines from input.txt
    with open(r"E:\advent\input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]      # 'L' or 'R'
            steps = int(line[1:])    # number after L/R

            if direction == 'L':
                position = (position - steps) % 100
            else:  # direction == 'R'
                position = (position + steps) % 100

            # check if we landed on 0
            if position == 0:
                count_zero += 1

    print("Password:", count_zero)


# run the solution
if __name__ == "__main__":
    solve()
