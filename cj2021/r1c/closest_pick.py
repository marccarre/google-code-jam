'''
$ python cj2021/r1c/closest_pick.py < tests/cj2021/r1c/closest_pick.txt
Case #1: 0.5
Case #2: 0.4
Case #3: 0.0
Case #4: 0.25

'''

from typing import List, Tuple


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        n, k = [int(x) for x in input().split()]
        purchased = [int(x) for x in input().split()]
        assert len(purchased) == n
        proba = calc_proba(n, k, purchased)
        print('Case #%d: %s' % (i, proba))


def calc_proba(n: int, k: int, purchased: List[int]) -> float:
    taken = [False] * k
    for p in purchased:
        taken[p - 1] = True
    l_dist = []
    for i in range(k):
        if taken[i]:
            l_dist.append(0)
        elif not l_dist:
            l_dist.append(1)
        else:
            l_dist.append(l_dist[-1] + 1)
    r_dist = []
    for i in range(k - 1, -1, -1):
        if taken[i]:
            r_dist.append(0)
        elif not r_dist:
            r_dist.append(1)
        else:
            r_dist.append(r_dist[-1] + 1)
    r_dist.reverse()
    dist = [0] * k
    for i in range(k):
        if k - i == r_dist[i]:
            dist[i] = r_dist[i]
            break
        else:
            dist[i] = min(l_dist[i], r_dist[i])
    d0, i = __find_max(dist)
    dist[i] = 0
    d1, _ = __find_max(dist)
    return (d0 + d1) / k


def __find_max(xs: List[int]) -> Tuple[int, int]:
    max_x, idx_max = 0, 0
    for i, x in enumerate(xs):
        if x > max_x:
            max_x, idx_max = x, i
    return max_x, idx_max


if __name__ == '__main__':
    main()
