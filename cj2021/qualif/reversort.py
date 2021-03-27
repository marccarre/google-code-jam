from typing import List


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        n = int(input())
        l = [int(x) for x in input().split()]
        assert len(l) == n
        out = reversort(l)
        print('Case #%d: %s' % (i, out))


def reversort(l: List[int]) -> int:
    n = len(l)
    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            l[lo], l[hi] = l[hi], l[lo]
            lo += 1
            hi -= 1
    def min_idx(lo: int) -> int:
        idx_min_v, min_v = lo, l[lo]
        for k in range(lo, n):
            if l[k] < min_v:
                min_v, idx_min_v = l[k], k
        return idx_min_v
    cost = 0
    for i in range(len(l) - 1):
        j = min_idx(i)
        reverse(i, j)
        cost += j - i + 1
        # print(i, j, cost, l)
    return cost


if __name__ == '__main__':
    main()
