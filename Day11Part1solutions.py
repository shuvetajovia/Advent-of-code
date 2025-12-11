from collections import defaultdict

def count_paths_from_file(path):
    graph = defaultdict(list)

    # Read file
    with open(path, "r") as f:
        for line in f:
            if ":" not in line:
                continue
            left, right = line.split(":")
            left = left.strip()
            targets = right.strip().split()
            graph[left].extend(targets)

    # DFS to count paths
    path_count = 0

    def dfs(node):
        nonlocal path_count
        if node == "out":
            path_count += 1
            return
        for nxt in graph[node]:
            dfs(nxt)

    dfs("you")
    return path_count


# Run
print(count_paths_from_file(r"E:\advent\input.txt"))
