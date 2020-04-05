from pytest import main
from cj2020.qualif.vestigium import trace_and_duplicates


def test_trace_and_duplicates():
    assert trace_and_duplicates([
        [1, 2, 3, 4],
        [2, 1, 4, 3],
        [3, 4, 1, 2],
        [4, 3, 2, 1],
    ]) == (4, 0, 0)

    assert trace_and_duplicates([
        [2, 2, 2, 2],
        [2, 3, 2, 3],
        [2, 2, 2, 3],
        [2, 2, 2, 2],
    ]) == (9, 4, 4)

    assert trace_and_duplicates([
        [2, 1, 3],
        [1, 3, 2],
        [1, 2, 3],
    ]) == (8, 0, 2)


if __name__ == '__main__':
    main()
