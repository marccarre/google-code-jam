'''
Qualification Round 2020 - Code Jam 2020
Indicium (7pts, 25pts)

Problem
Indicium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

A Latin square is an N-by-N square matrix in which each cell contains one of N different values, such that no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).

Given values N and K, produce any N-by-N "natural Latin square" with trace K, or say it is impossible. For example, here are two possible answers for N = 3, K = 6. In each case, the values that contribute to the trace are underlined.

2 1 3   3 1 2
3 2 1   1 2 3
1 3 2   2 3 1

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line containing two integers N and K: the desired size of the matrix and the desired trace.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if there is no answer for the given parameters or POSSIBLE otherwise. In the latter case, output N more lines of N integers each, representing a valid "natural Latin square" with a trace of K, as described above.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
N ≤ K ≤ N2.

Test set 1 (Visible Verdict)
T = 44.
2 ≤ N ≤ 5.

Test set 2 (Hidden Verdict)
1 ≤ T ≤ 100.
2 ≤ N ≤ 50.

Sample

Input

Output

2
3 6
2 3


Case #1: POSSIBLE
2 1 3
3 2 1
1 3 2
Case #2: IMPOSSIBLE


Sample Case #1 is the one described in the problem statement.

Sample Case #2 has no answer. The only possible 2-by-2 "natural Latin squares" are as follows:

1 2   2 1
2 1   1 2
These have traces of 2 and 4, respectively. There is no way to get a trace of 3.
'''


from typing import List, Optional, Set, Tuple


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        n, k = [int(x) for x in input().split()]
        status, matrix = n_k_trace(n, k)
        print('Case #%d: %s' % (i, status))
        if matrix:
            print_matrix(matrix)


def n_k_trace(n: int, k: int) -> Tuple[str, Optional[List[List[int]]]]:
    for trace in n_k_traces(n, k):
        matrix = partial_matrix_with_trace(n, trace)
        matrix = solve(matrix, k)
        if matrix:
            return 'POSSIBLE', matrix
    return 'IMPOSSIBLE', None

def n_k_traces(n: int, k: int):
    def recurse(size: int, k: int):
        if size == 1:
            if 1 <= k <= n:
                yield (k,)
        else:
            for i in range(1, n + 1):
                for permutation in recurse(size - 1, k - i):
                    yield (i,) + permutation
    yield from recurse(n, k)

def partial_matrix_with_trace(n: int, trace: Tuple[int]) -> List[List[int]]:
    matrix = [[None] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = trace[i]
    return matrix

def solve(matrix: List[List[int]], k: int) -> Optional[List[List[int]]]:
    if is_filled(matrix):
        return matrix
    i, j = next_empty_cell(matrix)
    search_space = possible_values(matrix, i, j)
    if not search_space:
        return None
    for x in search_space:
        matrix[i][j] = x
        m = solve(copy_matrix(matrix), k)
        if m:
            return m
    return None

def is_filled(matrix: List[List[int]]) -> bool:
    return all(cell is not None for row in matrix for cell in row)

def next_empty_cell(matrix: List[List[int]]) -> Tuple[int, int]:
    '''
    Find the empty cell with the minimum degree of freedom, in order to speed up the resolution.
    For example, given:

         0    1    2    3
       +---------------------+ min:
     0 | None None None 1    | 3
     1 | None 1    1    1    | 1
     2 | None 1    None None | 3
     3 | None 1    1    None | 2
       +---------------------+
    min: 4    1    2    2

    we'd want to next pick either (0, 1) or (3, 3).
    '''
    n = len(matrix)
    min_empty = n + n
    min_coords = (-1, -1)
    row_count = empty_cells_by_row(matrix)
    col_count = empty_cells_by_col(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] is None and row_count[i] + col_count[j] < min_empty:
                min_empty = row_count[i] + col_count[j]
                min_coords = (i, j)
    return min_coords


def empty_cells_by_row(matrix: List[List[int]]) -> List[int]:
    row_count = []
    for row in matrix:
        row_count.append(sum(cell is None for cell in row))
    return row_count

def empty_cells_by_col(matrix: List[List[int]]) -> List[int]:
    col_count = []
    for j in range(len(matrix)):
        col_count.append(sum(cell is None for cell in col(j, matrix)))
    return col_count

def possible_values(matrix: List[List[int]], row: int, col: int) -> Set[int]:
    n = len(matrix)
    # Look at current row, and remove values already used from the search space:
    row_universe = set(range(1, n + 1))
    for j in range(n):
        if matrix[row][j] in row_universe:
            row_universe.remove(matrix[row][j])
    # Look at current col, and remove values already used from the search space:
    col_universe = set(range(1, n + 1))
    for i in range(n):
        if matrix[i][col] in col_universe:
            col_universe.remove(matrix[i][col])
    return row_universe.intersection(col_universe)

def col(j: int, matrix: List[List[int]]) -> List[int]:
    return [row[j] for row in matrix]

def copy_matrix(matrix: List[List[int]]) -> List[List[int]]:
    return [row[:] for row in matrix]

def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(' '.join(str(x) for x in row))


if __name__ == '__main__':
    main()
