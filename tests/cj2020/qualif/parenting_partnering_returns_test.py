from pytest import main
from cj2020.qualif.parenting_partnering_returns import schedule


def test_schedule():
    assert schedule([[360, 480], [420, 540], [600, 660]]) == 'CJC'
    assert schedule([[0, 1440], [1, 3], [2, 4]]) == 'IMPOSSIBLE'
    assert schedule([[99, 150], [1, 100], [100, 301], [2, 5], [150, 250]]) == 'JCCJJ'
    assert schedule([[0, 720], [720, 1440]]) == 'CC'


if __name__ == '__main__':
    main()
