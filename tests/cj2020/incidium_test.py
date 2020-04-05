from pytest import main
from cj2020.incidium import n_k_trace, next_empty_cell, possible_values


def test_n_k_trace():
    assert n_k_trace(3, 6) == ('POSSIBLE', [
        [1, 3, 2],
        [3, 2, 1],
        [2, 1, 3],
    ])
    assert n_k_trace(2, 3) == ('IMPOSSIBLE', None)
    assert n_k_trace(4, 7) == ('POSSIBLE', [
        [1, 2, 3, 4],
        [3, 1, 4, 2],
        [4, 3, 2, 1],
        [2, 4, 1, 3],
    ])
    assert n_k_trace(4, 16) == ('POSSIBLE', [
        [4, 1, 2, 3],
        [3, 4, 1, 2],
        [2, 3, 4, 1],
        [1, 2, 3, 4],
    ])


def test_next_empty_cell():
    matrix = [
        [None, None, None, 2],
        [None, 1,    2,    3],
        [None, 2,    None, None],
        [None, 3,    1,    None],
    ]
    assert next_empty_cell(matrix) == (0, 1)
    matrix[0][1] = 4
    assert next_empty_cell(matrix) == (0, 2)
    matrix[0][2] = 3
    assert next_empty_cell(matrix) == (2, 2)
    matrix[2][2] = 4
    assert next_empty_cell(matrix) == (2, 3)
    matrix[2][3] = 1
    assert next_empty_cell(matrix) == (3, 3)


def test_possible_values():
    matrix = [
        [None, None, None, 2],
        [None, 1,    2,    3],
        [None, 2,    None, None],
        [None, 3,    1,    None],
    ]
    assert possible_values(matrix, 0, 1) == set([4])
    assert possible_values(matrix, 3, 3) == set([4])


if __name__ == '__main__':
    main()
