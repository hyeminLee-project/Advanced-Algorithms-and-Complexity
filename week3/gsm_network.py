# python3
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]

def printEquisatisfiableSatFormula():
    clauses = []
    num_vars = n * 3  # 각 정점마다 3개의 색을 할당하므로 변수의 총 개수는 n * 3
    # Helper function to encode variables
    def var(vertex, color):
        return (vertex - 1) * 3 + color

    # 각 정점은 하나의 색을 가져야 한다.
    for i in range(1, n + 1):
        # (x_{i1} OR x_{i2} OR x_{i3})
        clauses.append([var(i, 1), var(i, 2), var(i, 3)])

        # (¬x_{i1} OR ¬x_{i2}), (¬x_{i1} OR ¬x_{i3}), (¬x_{i2} OR ¬x_{i3})
        clauses.append([-var(i, 1), -var(i, 2)])
        clauses.append([-var(i, 1), -var(i, 3)])
        clauses.append([-var(i, 2), -var(i, 3)])

    # 인접한 정점은 서로 다른 색을 가져야 한다.
    for u, v in edges:
        for color in range(1, 4):  # 색은 1, 2, 3
            # (¬x_{u_color} OR ¬x_{v_color})
            clauses.append([-var(u, color), -var(v, color)])

    # 출력
    print(len(clauses), num_vars)  # 절의 수와 변수의 수 출력
    for clause in clauses:
        print(" ".join(map(str, clause)) + " 0")

printEquisatisfiableSatFormula()
