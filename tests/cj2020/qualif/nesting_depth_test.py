from pytest import main
from cj2020.qualif.nesting_depth import nest


def test_nest():
    assert nest('0000') == '0000'
    assert nest('101') == '(1)0(1)'
    assert nest('111000') == '(111)000'
    assert nest('1') == '(1)'
    assert nest('31') == '(((3))1)'


if __name__ == '__main__':
    main()
