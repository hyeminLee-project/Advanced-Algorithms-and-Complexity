# python3
from itertools import permutations
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0  # 자기 자신으로의 이동 비용은 0
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def optimal_path(graph):
    n = len(graph)
    dp = [[INF] * n for _ in range(1 << n)]  # dp[mask][i]: mask 상태에서 i번 정점에 도달하는 최소 비용
    dp[1][0] = 0  # 시작점(0번 정점)에서 시작, 상태는 1(000...1)

    # 상태 전이
    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):  # u가 현재 mask에 포함되지 않은 경우
                continue
            for v in range(n):
                if mask & (1 << v):  # v가 이미 방문된 경우
                    continue
                dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + graph[u][v])

    # 최소 비용 계산 및 경로 추적
    full_mask = (1 << n) - 1  # 모든 정점을 방문한 상태
    min_cost = INF
    last_node = -1

    for u in range(1, n):
        if dp[full_mask][u] + graph[u][0] < min_cost:
            min_cost = dp[full_mask][u] + graph[u][0]
            last_node = u

    if min_cost >= INF:
        return (-1, [])  # 가능한 경로가 없는 경우

    # 경로 추적
    path = [last_node]
    mask = full_mask
    while last_node != 0:
        for prev in range(n):
            if mask & (1 << prev) and dp[mask][last_node] == dp[mask ^ (1 << last_node)][prev] + graph[prev][last_node]:
                path.append(prev)
                mask ^= (1 << last_node)
                last_node = prev
                break

    path.reverse()
    return (min_cost, [x + 1 for x in path])

if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
