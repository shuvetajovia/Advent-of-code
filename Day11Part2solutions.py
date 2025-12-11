from collections import defaultdict
from functools import cache
from typing import Dict, List

INPUT_FILE = r"E:\advent\input.txt"


def parse_data(path: str) -> Dict[str, List[str]]:
    graph = defaultdict(list)

    with open(path) as f:
        contents = f.read()

    for line in contents.strip().split("\n"):
        if not line.strip():
            continue

        try:
            input_node, outputs_raw = line.split(": ")
        except ValueError:
            print("Bad line:", line)
            continue

        outputs = outputs_raw.split(" ")
        graph[input_node] = outputs

    return graph


def solve_one(data: Dict[str, List[str]]) -> int:
    def paths(node: str) -> int:
        if node == "out":
            return 1

        p = 0
        for output in data[node]:
            p += paths(output)
        return p

    return paths("you")


def solve_two(data: Dict[str, List[str]]) -> int:
    @cache
    def paths(node: str, dac: bool, fft: bool) -> int:
        if node == "out":
            return int(dac and fft)

        p = 0
        for output in data[node]:
            dac_p = output == "dac" or dac
            fft_p = output == "fft" or fft
            p += paths(output, dac_p, fft_p)
        return p

    return paths("svr", False, False)


def main():
    data = parse_data(INPUT_FILE)
    print("Part 2:", solve_two(data))


if __name__ == "__main__":
    main()
