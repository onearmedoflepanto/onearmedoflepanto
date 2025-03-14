def is_connected(group):
    """group에 속한 노드들이 연결되어 있는지 검사하는 함수."""
    if not group:
        return False
    visited = set()
    stack = [group[0]]
    group_set = set(group)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in group_set and neighbor not in visited:
                    stack.append(neighbor)
    return len(visited) == len(group)


def dfs(idx, subset):
    global mindiff
    if idx == n:
        if len(subset) == 0 or len(subset) == n:
            return
        complement = [i for i in range(n) if i not in subset]
        if is_connected(subset) and is_connected(complement):
            diff = abs(sum(nodes[i] for i in subset) -
                       sum(nodes[i] for i in complement))
            mindiff = min(mindiff, diff)
        return

    dfs(idx + 1, subset)

    subset.append(idx)
    dfs(idx + 1, subset)
    subset.pop()


tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph_arr = [list(map(int, input().split())) for _ in range(n)]
    nodes = list(map(int, input().split()))

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_arr[i][j] == 1:
                graph[i].append(j)

    mindiff = float('inf')
    dfs(1, [0])

    result = mindiff if mindiff != float('inf') else -1
    print(f"#{t} {result}")
