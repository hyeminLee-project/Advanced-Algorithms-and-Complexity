# python3
EPS = 1e-6
PRECISION = 6

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input().strip())
    if size == 0:
        exit(0)
    a = []
    b = []
    for _ in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    size = len(a)
    for col in range(size):
        if not used_columns[col]:
            for row in range(size):
                if not used_rows[row] and abs(a[row][col]) > EPS:
                    return Position(col, row)
    raise ValueError("No valid pivot found, the system may be singular or nearly singular.")

def SwapLines(a, b, used_rows, pivot_element):
    if pivot_element.row != pivot_element.column:
        a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
        b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
        used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot_element):
    size = len(a)
    pivot_row = pivot_element.row
    pivot_column = pivot_element.column
    pivot_value = a[pivot_row][pivot_column]

    if abs(pivot_value) < EPS:
        raise ValueError("Pivot element is too small, leading to numerical instability.")

    for col in range(size):
        a[pivot_row][col] /= pivot_value
    b[pivot_row] /= pivot_value

    for row in range(size):
        if row != pivot_row:
            factor = a[row][pivot_column]
            for col in range(size):
                a[row][col] -= factor * a[pivot_row][col]
            b[row] -= factor * b[pivot_row]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("{:.{precision}f}".format(column[row], precision=PRECISION))

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
