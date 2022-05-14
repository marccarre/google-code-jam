from typing import List


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        r, c = [int(x) for x in input().split()]
        card = draw_card(r, c)
        print('Case #%d:\n%s' % (i, card))


def draw_card(r: int, c: int) -> str:
    lines = []

    line = ['..+']
    for _ in range(c - 1):
        line.append('-+')
    lines.append(''.join(line))

    line = ['..|']
    for _ in range(c - 1):
        line.append('.|')
    lines.append(''.join(line))

    line = ['+']
    for _ in range(c):
        line.append('-+')
    lines.append(''.join(line))

    for _ in range(r - 1):
        line = ['|']
        for _ in range(c):
            line.append('.|')
        lines.append(''.join(line))
        line = ['+']
        for _ in range(c):
            line.append('-+')
        lines.append(''.join(line))

    return '\n'.join(lines)


if __name__ == '__main__':
    main()
