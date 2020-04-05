from typing import Tuple


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        n = int(input())
        a, b = split_without_any_four(n)
        print('Case #%d: %d %d' % (i, a, b))


def split_without_any_four(n: int) -> Tuple[int, int]:
    a, b = [], []
    for c in str(n):
        if c == '4':
            a.append('2')
            b.append('2')
        else:
            a.append(c)
            b.append('0')
    return int(''.join(a)), int(''.join(b))


if __name__ == '__main__':
    main()
