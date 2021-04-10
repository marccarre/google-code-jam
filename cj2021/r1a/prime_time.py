'''
python cj2021/r1a/prime_time.py < tests/cj2021/r1a/prime_time.txt
'''

from collections import Counter
from itertools import chain, combinations
from functools import reduce
from operator import mul
from typing import Dict, List, Tuple


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        m = int(input())
        # cards = Counter()
        cards = []
        for _ in range(m):
            p, n = [int(x) for x in input().split()]
            # cards[p] = n
            cards.extend([p] * n)
        score = play(cards)
        print('Case #%d: %s' % (i, score))


def play(cards_list: List[int]) -> int:
    cards = Counter(cards_list)
    max_score = 0
    for cards_set in _powerset(cards_list):
        if not cards_set:
            continue
        s = sum(cards_set)
        p = reduce(mul, cards_set)
        remainder = cards - Counter(cards_set)
        if not remainder:
            continue
        s_r = _sum(remainder)
        p_r = _product(remainder)
        score = 0
        if s == p_r:
            score = max(score, s)
        if p == s_r:
            score = max(score, p)
        max_score = max(max_score, score)
    return max_score


def _sum(d: Dict[int, int]) -> int:
    s = 0
    for v, count in d.items():
        s += v * count
    return s


def _product(d: Dict[int, int]) -> int:
    p = 0
    for v, count in d.items():
        p *= v ** count
    return p


def _powerset(s: List[int]) -> List[Tuple[int]]:
    ''' _powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3) '''
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


if __name__ == '__main__':
    main()
