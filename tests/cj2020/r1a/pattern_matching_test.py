from pytest import main
from cj2020.r1a.pattern_matching import min_word


def test_min_word():
    assert min_word(['*CONUTS', '*COCONUTS', '*OCONUTS', '*CONUTS', '*S']) == 'COCONUTS'
    assert min_word(['*XZ', '*XYZ']) == '*'

    assert min_word(['H*O', 'HELLO*', '*HELLO', 'HE*']) == 'HELLOHELLO'
    assert min_word(['CO*DE', 'J*AM']) == '*'
    assert min_word(['CODE*', '*JAM']) == 'CODEJAM'

    # assert min_word(['A*C*E', '*B*D*']) == 'ABCDE'
    # assert min_word(['A*C*E', '*B*D']) == '*'
    # assert min_word(['**Q**', '*A*']) == 'AQ'


if __name__ == '__main__':
    main()
