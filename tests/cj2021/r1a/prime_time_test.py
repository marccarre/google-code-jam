from pytest import main
from cj2021.r1a.prime_time import play


def test_play():
    assert play([2, 2, 3, 5, 5, 7, 11]) == 25
    assert play([17, 17]) == 17
    assert play([2, 2, 3]) == 0
    assert play([2, 2, 2, 2, 2, 2, 2]) == 8


if __name__ == '__main__':
    main()
