from pytest import main
from cj2022.r1a.double_or_one_thing import first_string


def test_first_string():
    assert first_string('PEEL') == 'PEEEEL'
    assert first_string('AAAAAAAAAA') == 'AAAAAAAAAA'
    assert first_string('CODEJAMDAY') == 'CCODDEEJAAMDAAY'


if __name__ == '__main__':
    main()
