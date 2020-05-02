from pytest import main
from cj2020.r1c.overexcited_fan import meet_peppurr


def test_meet_peppurr():
    assert meet_peppurr((4, 4), 'SSSS') == 4
    assert meet_peppurr((3, 0), 'SNSS') == 'IMPOSSIBLE'
    assert meet_peppurr((2, 10), 'NSNNSN') == 'IMPOSSIBLE'
    assert meet_peppurr((0, 1), 'S') == 1
    assert meet_peppurr((2, 7), 'SSSSSSSS') == 5
    assert meet_peppurr((3, 2), 'SSSW') == 4
    assert meet_peppurr((4, 0), 'NESW') == 4


if __name__ == '__main__':
    main()
