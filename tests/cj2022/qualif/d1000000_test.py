from pytest import main
from cj2022.qualif.d1000000 import longest_straight


def test_longest_straight():
    assert longest_straight([6, 10, 12, 8]) == 4
    assert longest_straight([5, 4, 5, 4, 4, 4]) == 5
    assert longest_straight([10, 10, 7, 6, 7, 4, 4, 5, 7, 4]) == 9
    assert longest_straight([10]) == 1


if __name__ == '__main__':
    main()
