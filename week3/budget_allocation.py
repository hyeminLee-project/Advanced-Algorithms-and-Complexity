#Python 3
from sys import stdin

def printEquisatisfiableSatFormula():
    n, m = map(int, stdin.readline().split())
    A = []
    for _ in range(n):
        A.append(list(map(int, stdin.readline().split())))
    b = list(map(int, stdin.readline().split()))

    clauses = []

    for i in range(n):
        non_zero_coeffs = [(j, A[i][j]) for j in range(m) if A[i][j] != 0]
        l = len(non_zero_coeffs)
        for x in range(2**l):
            current_set = [non_zero_coeffs[j] for j in range(l) if (x >> j) & 1]
            current_sum = sum(coeff[1] for coeff in current_set)
            if current_sum > b[i]:
                clause = []
                for coeff in non_zero_coeffs:
                    var_index = coeff[0] + 1
                    if coeff in current_set:
                        clause.append(-var_index)
                    else:
                        clause.append(var_index)
                clauses.append(clause)

    if not clauses:
        clauses.append([1, -1])
        m = 1

    print(len(clauses), m)
    for clause in clauses:
        print(" ".join(map(str, clause)) + " 0")

printEquisatisfiableSatFormula()
