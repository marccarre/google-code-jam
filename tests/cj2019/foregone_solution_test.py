from pytest import main
from cj2019.foregone_solution import split_without_any_four


def test_split_without_any_four():
    assert split_without_any_four(4) == (2, 2)
    assert split_without_any_four(940) == (920, 20)
    assert split_without_any_four(4444) == (2222, 2222)


if __name__ == '__main__':
    main()
