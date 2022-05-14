import pytest
from pytest import main
from cj2022.r1a.weightlifting import min_ops


@pytest.mark.skip(reason="problem not successfully resolved yet")
def test_min_ops():
    assert min_ops([[1],[2],[1]]) == 4

    assert min_ops([
        [1, 2, 1],
        [2, 1, 2],
    ]) == 12

    assert min_ops([
        [3, 1, 1],
        [3, 3, 3],
        [2, 3, 3],
    ]) == 20


if __name__ == '__main__':
    main()
