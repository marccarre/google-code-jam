from pytest import main
from cj2020.r1a.square_dance import interest_level


def test_interest_level():
    assert interest_level([[15]]) == 15
    assert interest_level([
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1],
    ]) == 16
    assert interest_level([[3, 1, 2]]) == 14
    assert interest_level([[1, 2, 3]]) == 14


if __name__ == '__main__':
    main()
