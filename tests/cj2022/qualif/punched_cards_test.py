from pytest import main
from cj2022.qualif.punched_cards import draw_card


def test_draw_card():
    assert draw_card(3, 4) == '''..+-+-+-+
..|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+'''
    assert draw_card(2, 2) == '''..+-+
..|.|
+-+-+
|.|.|
+-+-+'''

    assert draw_card(2, 3) == '''..+-+-+
..|.|.|
+-+-+-+
|.|.|.|
+-+-+-+'''


if __name__ == '__main__':
    main()


