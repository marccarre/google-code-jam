from pytest import main
from cj2021.qualif.moons_and_umbrellas import mau


def test_mau():
    assert mau(2, 3, 'CJ?CC?') == 5
    assert mau(4, 2, 'CJCJ') == 10
    assert mau(1, 3, 'C?J') == 1
    assert mau(2, 5, '??J???') == 0


if __name__ == '__main__':
    main()


