'''
$ python cj2021/r1c/double_or_noting.py < tests/cj2021/r1c/double_or_noting.txt
Case #1: 4
Case #2: 3
Case #3: 2
Case #4: 1
Case #5: IMPOSSIBLE
Case #6: 0

'''

from math import inf
from typing import List, Tuple


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        s, e = [x for x in input().split()]
        n = num_ops(s, e)
        if n < 0:
            n = 'IMPOSSIBLE'
        print('Case #%d: %s' % (i, n))


def num_ops(s: str, e: str) -> int:
    seen = set()
    def search(s: str, count: int):
        if s == e:
            return count
        if s in seen or len(s) > 2 * len(e):
            return inf
        seen.add(s)
        return min(
            search(''.join(['0' if c == '1' else '1' for c in s]), count + 1),
            search(bin(int(s, base=2) << 1)[2:], count + 1)
        )
    min_ops = search(s, 0)
    return -1 if min_ops == inf else min_ops


if __name__ == '__main__':
    main()
