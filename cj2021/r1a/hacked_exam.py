'''
python cj2021/r1a/hacked_exam.py < tests/cj2021/r1a/hacked_exam.txt
'''

from collections import Counter
from itertools import chain, combinations
from functools import reduce
from operator import mul
from typing import Dict, List, Tuple


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        n, q = [int(x) for x in input().split()]
        answers = {}
        for _ in range(n):
            a, s = input().split()
            assert len(a) == q
            answers[a] = int(s)
        y, z, w = hack(answers, q)
        print('Case #%d: %s %d/%d' % (i, y, z, w))


def hack(answers: Dict[str, int], q: int) -> Tuple[str, int, int]:
    max_score = 0
    for answer, score in answers.items():
        if score == q:
            return answer, score, 1
    return answer, score, 0


if __name__ == '__main__':
    main()
