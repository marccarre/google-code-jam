from pytest import main
from cj2021.qualif.reversort import reversort


def test_reversort():
    assert reversort([4, 2, 1, 3]) == 6
    assert reversort([1, 2]) == 1
    assert reversort([7, 6, 5, 4, 3, 2, 1]) == 12


if __name__ == '__main__':
    main()
