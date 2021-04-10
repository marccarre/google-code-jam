from pytest import main
from cj2021.r1a.append_sort import num_ops


def test_num_ops():
    assert num_ops([100, 7, 10]) == (4, [100, 700, 1000])
    assert num_ops([10, 10]) == (1, [10, 100])
    assert num_ops([4, 19, 1]) == (2, [4, 19, 100])
    assert num_ops([1, 2, 3]) == (0, [1, 2, 3])
    assert num_ops([98, 9]) == (1, [98, 99])
    assert num_ops([100, 10]) == (1, [100, 101])
    assert num_ops([1000, 10]) == (2, [1000, 1001])
    assert num_ops([10001, 10]) == (3, [10001, 10002])
    # assert num_ops([984882677, 983457724, 951345618, 950255435, 946163246, 934355312, 918545676, 909176550, 904548246, 886453830, 863047610, 857857210, 842668580, 836647416, 835889861, 829197136, 806828041, 803271726, 783639922, 765976864, 762797009, 760752874, 749918763, 747869561, 717957544, 703998227, 700932392, 693021090, 691723853, 691274181, 682352529, 653689110, 648904047, 634489072, 615941801, 600155194, 592637959, 568195587, 553895923, 550557514, 538655589, 533618144, 533554841, 528843488, 528285331, 528024964, 519903274, 506705367, 488030737, 488006374, 485068035, 473542873, 472834988, 470110877, 468682469, 455230447, 434209533, 429154935, 423568039, 421922037, 403638162, 400000407, 399611789, 387063475, 357021847, 354749303, 350956053, 348044552, 331554417, 327240277, 325521731, 310897820, 310469745, 302559069, 300677844, 290480523, 289741268, 274353641, 265013457, 247243521, 239221345, 226420626, 224265813, 193864738, 182517264, 158601813, 124014337, 118811119, 105796911, 101055211, 101055211, 101055211, 101055211, 101055211, 101055211, 101055211, 101055211, 101055211, 101055211, 101055211]) == (4896, [])


if __name__ == '__main__':
    main()
