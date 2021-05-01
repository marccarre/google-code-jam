from pytest import main
from cj2021.r1c.closest_pick import calc_proba


def test_calc_proba():
    assert calc_proba(3, 10, [1, 3, 7]) == 0.5
    assert calc_proba(4, 10, [4, 1, 7, 3]) == 0.4
    assert calc_proba(4, 3, [1, 2, 3, 2]) == 0.0
    assert calc_proba(4, 4, [1, 2, 4, 2]) == 0.25


if __name__ == '__main__':
    main()
