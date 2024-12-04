#uses python3
import sys
import threading

# Stack overflow 방지 설정
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for _ in range(size - 1):
        a, b = map(int, input().split())
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, dp):
    include = tree[vertex].weight  # 현재 노드를 초대하는 경우
    exclude = 0  # 현재 노드를 초대하지 않는 경우

    for child in tree[vertex].children:
        if child != parent:  # 부모 노드는 다시 방문하지 않음
            dfs(tree, child, vertex, dp)
            include += dp[child][0]  # 자식이 초대되지 않은 경우
            exclude += max(dp[child][0], dp[child][1])  # 자식을 초대하거나 초대하지 않거나 중 최대값

    dp[vertex][0] = exclude
    dp[vertex][1] = include


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0

    dp = [[0, 0] for _ in range(size)]  # dp[u][0]: u를 초대하지 않은 경우, dp[u][1]: u를 초대한 경우
    dfs(tree, 0, -1, dp)  # 루트 노드에서 DFS 시작
    return max(dp[0][0], dp[0][1])  # 루트 노드의 두 경우 중 최대값 반환


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# Stack overflow 방지 설정
threading.Thread(target=main).start()
