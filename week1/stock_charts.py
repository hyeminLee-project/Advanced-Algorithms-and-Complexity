# python3
class MinimumPathCoverDAG:
    def __init__(self, stock_data):
        self.stock_data = stock_data
        self.n = len(stock_data)
        self.graph = [[] for _ in range(self.n)]
        self.left_match = [-1] * self.n
        self.right_match = [-1] * self.n

    def can_place_together(self, stock1, stock2):
        return all(x < y for x, y in zip(stock1, stock2))

    def build_dag(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.can_place_together(self.stock_data[i], self.stock_data[j]):
                    self.graph[i].append(j)

    def dfs(self, u, visited):
        for v in self.graph[u]:
            if not visited[v]:
                visited[v] = True
                if self.right_match[v] == -1 or self.dfs(self.right_match[v], visited):
                    self.right_match[v] = u
                    self.left_match[u] = v
                    return True
        return False

    def max_matching(self):
        match_count = 0
        for u in range(self.n):
            visited = [False] * self.n
            if self.dfs(u, visited):
                match_count += 1
        return match_count

    def minimum_path_cover(self):
        self.build_dag()
        max_match = self.max_matching()
        return self.n - max_match

    @staticmethod
    def solve():
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for _ in range(n)]
        mpc_dag = MinimumPathCoverDAG(stock_data)
        result = mpc_dag.minimum_path_cover()
        print(result)

if __name__ == '__main__':
    MinimumPathCoverDAG.solve()