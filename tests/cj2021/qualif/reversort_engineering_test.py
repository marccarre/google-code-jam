import pytest
from pytest import main
from cj2021.qualif.reversort_engineering import reversort_engineering


@pytest.mark.skip(reason='bug')
def test_reversort_engineering():
    assert reversort_engineering(4, 6) == [4, 2, 1, 3]
    assert reversort_engineering(2, 1) == [1, 2]
    assert reversort_engineering(7, 12) == [7, 6, 5, 4, 3, 2, 1]
    assert reversort_engineering(7, 2) == 'IMPOSSIBLE'
    assert reversort_engineering(2, 1000) == 'IMPOSSIBLE'


if __name__ == '__main__':
    main()
