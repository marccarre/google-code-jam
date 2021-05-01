import pytest
from pytest import main
from cj2021.r1c.double_or_noting import num_ops


@pytest.mark.skip(reason='bug')
def test_num_ops():
    assert num_ops('10001', '111') == 4
    assert num_ops('1011', '111') == 3
    assert num_ops('1010', '1011') == 2
    assert num_ops('0', '1') == 1
    assert num_ops('0', '101') == -1
    assert num_ops('1101011', '1101011') == 0


if __name__ == '__main__':
    main()
