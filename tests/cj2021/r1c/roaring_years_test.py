from pytest import main
from cj2021.r1c.roaring_years import next_year


def test_next_year():
    assert next_year(2020) == 2021
    assert next_year(2021) == 2122
    assert next_year(68000) == 78910
    assert next_year(101) == 123


if __name__ == '__main__':
    main()
