from functools import lru_cache
from typing import List


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        n, cost = [int(x) for x in input().split()]
        out = reversort_engineering(n, cost)
        if out != IMPOSSIBLE:
            out = ' '.join([str(x) for x in out])
        print('Case #%d: %s' % (i, out))


IMPOSSIBLE = 'IMPOSSIBLE'


def reversort_engineering(n: int, cost: int) -> int:
    if n - 1 > cost:
        return IMPOSSIBLE
    if n * (n + 1) // 2 <= cost:
        return IMPOSSIBLE

    l = [None] * (n + 1)
    curr, lo, hi = 1, 1, n
    up = True
    while lo < hi and (hi - lo) * 2 - 1 < cost:
        cost -= hi - lo + 1
        if up:
            l[hi] = curr
            hi -= 1
        else:
            l[lo] = curr
            lo += 1
        up = not up
        curr += 1

    if up:
        while cost <= (hi - lo) * 2 - 1:
            l[lo] = curr
            lo += 1
            curr += 1
            cost -= 1
        for i in range(hi, lo - 1, -1):
            l[i] = curr
            curr += 1
    else:
        while cost <= (hi - lo) * 2 - 1:
            l[hi] = curr
            hi -= 1
            curr += 1
            cost -= 1
        for i in range(lo, hi + 1):
            l[i] = curr
            curr += 1
    return l[1:]


'''
    @lru_cache(maxsize=None)
    def recurse(lo: int, n: int, remainder: int):
        if remainder < 0:
            return IMPOSSIBLE
        if remainder == 0:
            return l
        rng = max(nums) - min(nums) + 1
        for size in range(min(rng, remainder)):
            for i in range(lo, size):
                res = recurse(i, size, remainder)
    return recurse(0, n, cost - n + 1)
'''


if __name__ == '__main__':
    main()
