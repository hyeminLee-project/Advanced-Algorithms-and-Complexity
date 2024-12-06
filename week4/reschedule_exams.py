# python3
def assign_new_colors(n, edges, colors):
    # 그래프 생성
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # 초기화
    new_colors = [None] * n
    available_colors = {'R', 'G', 'B'}

    # DFS 함수
    def dfs(node):
        for neighbor in graph[node]:
            if new_colors[neighbor] == new_colors[node]:
                return False  # 인접한 정점이 같은 색이면 불가능
        for neighbor in graph[node]:
            if new_colors[neighbor] is None:  # 방문하지 않은 정점만 처리
                forbidden_colors = {new_colors[node]} | {new_colors[n] for n in graph[neighbor] if new_colors[n] is not None}
                valid_colors = available_colors - forbidden_colors
                if not valid_colors:
                    return False  # 가능한 색이 없으면 불가능
                new_colors[neighbor] = valid_colors.pop()
                if not dfs(neighbor):
                    return False
        return True

    # 색칠 가능한지 확인
    for i in range(n):
        if new_colors[i] is None:  # 아직 방문하지 않은 정점
            forbidden_colors = {colors[i]}  # 초기 색은 사용 불가
            valid_colors = available_colors - forbidden_colors
            if not valid_colors:
                return None  # 가능한 색이 없으면 불가능
            new_colors[i] = valid_colors.pop()
            if not dfs(i):
                return None

    # 최종 검증: 간선을 확인하여 인접한 정점이 같은 색인지 확인
    for u, v in edges:
        if new_colors[u - 1] == new_colors[v - 1]:
            return None  # 인접한 정점이 같은 색이면 불가능

    return new_colors

def main():
    n, m = map(int, input().split())
    colors = list(input().strip())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    new_colors = assign_new_colors(n, edges, colors)
    if new_colors is None:
        print("Impossible")
    else:
        print(''.join(new_colors))

main()
