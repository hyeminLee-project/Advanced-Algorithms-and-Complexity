# python3
class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for _ in range(n)]
        return adj_matrix

    def write_response(self, matching):
        # Outputs the matching in the required format
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        # Matching array where -1 means no match for a node
        matching = [-1] * m

        def bipartite_match(left, visited):
            # Try to find a match for left node `left`
            for right in range(m):
                if adj_matrix[left][right] and not visited[right]:
                    visited[right] = True
                    # If right node is not matched or if previously matched node can find alternative
                    if matching[right] == -1 or bipartite_match(matching[right], visited):
                        matching[right] = left
                        return True
            return False

        # For each left node, try to find a matching
        for left in range(n):
            visited = [False] * m
            bipartite_match(left, visited)

        # Convert matching array to required format (left -> right or -1 if no match)
        result = [-1] * n
        for right in range(m):
            if matching[right] != -1:
                result[matching[right]] = right

        return result

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()