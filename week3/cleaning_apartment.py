# python3
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]

def printEquisatisfiableSatFormula():
    clauses = []
    variables = n * n  # 각 방(i)와 위치(j)를 나타내는 변수 x_{ij}

    # Helper function to encode variables
    def var(vertex, position):
        return (vertex - 1) * n + position

    # 1. 각 방은 경로의 정확히 한 위치에 있어야 한다.
    for i in range(1, n + 1):
        clauses.append([var(i, j) for j in range(1, n + 1)])  # (x_{i1} OR x_{i2} OR ... OR x_{in})
        for j in range(1, n + 1):
            for k in range(j + 1, n + 1):
                clauses.append([-var(i, j), -var(i, k)])  # (¬x_{ij} OR ¬x_{ik})

    # 2. 각 위치에는 정확히 하나의 방만 있어야 한다.
    for j in range(1, n + 1):
        clauses.append([var(i, j) for i in range(1, n + 1)])  # (x_{1j} OR x_{2j} OR ... OR x_{nj})
        for i in range(1, n + 1):
            for k in range(i + 1, n + 1):
                clauses.append([-var(i, j), -var(k, j)])  # (¬x_{ij} OR ¬x_{kj})

    # 3. 경로의 연속된 방들은 반드시 연결되어 있어야 한다.
    edge_set = set((min(u, v), max(u, v)) for u, v in edges)  # 간선을 빠르게 확인하기 위해 집합 사용
    for j in range(1, n):  # 경로의 위치 1부터 n-1까지
        for i in range(1, n + 1):
            for k in range(1, n + 1):
                if i != k and (min(i, k), max(i, k)) not in edge_set:
                    clauses.append([-var(i, j), -var(k, j + 1)])  # (¬x_{ij} OR ¬x_{k(j+1)})

    # 출력
    print(len(clauses), variables)
    for clause in clauses:
        print(" ".join(map(str, clause)) + " 0")

printEquisatisfiableSatFormula()
