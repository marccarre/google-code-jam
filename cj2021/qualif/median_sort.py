'''
python cj2021/qualif/median_sort/interactive_runner.py \
    python cj2021/qualif/median_sort/local_testing_tool.py 0 -- \
    python cj2021/qualif/median_sort.py
'''
import heapq
import sys


DEBUG = True


def main() -> None:
    t, n, q = [int(x) for x in input().split()]
    for _ in range(t):
        solve(n, q)


def solve(n, max_q) -> None:
    heap = [(n, 1), (2 * n, 2)]
    q = 0
    for c in range(3, n + 1):
        idx_a, a = heapq.heappop(heap)
        idx_b, b = heapq.heappop(heap)
        print('%d %d %d' % (a, b, c))
        q += 1
        if DEBUG:
            print('%d %d %d' % (a, b, c), file=sys.stderr)
        median = int(input())
        if a == median:
            idx_c = idx_a // 2
        elif b == median:
            idx_c = 2 * idx_b
        elif c == median:
            idx_c = idx_a + (idx_b - idx_a) // 2
        else:
            raise RuntimeError('ERROR: unexpected median: %d' % median)
        heapq.heappush(heap, (idx_a, a))
        heapq.heappush(heap, (idx_b, b))
        heapq.heappush(heap, (idx_c, c))
        if DEBUG:
            print('%s' % heap, file=sys.stderr)

    IDX, VAL = 0, 1
    stack = []
    while q < max_q and len(set([idx for idx, _ in heap])) != n:
        if not stack:
            idx_a, a = heapq.heappop(heap)
            stack.append((idx_a, a))
            idx_b, b = heapq.heappop(heap)
            stack.append((idx_b, b))
        else:
            idx_a, a = stack[-2]
            idx_b, b = stack[-1]
        idx_c, c = heapq.heappop(heap)
        if idx_b == idx_c:
            print('%d %d %d' % (a, b, c))
            q += 1
            median = int(input())
            if a == median:
                raise RuntimeError('ERROR: bug?!')
            elif b == median:
                pass
            elif c == median:
                idx_c = idx_a + (idx_b - idx_a) // 2
                stack.pop()
                stack.append((idx_c, c))
            else:
                raise RuntimeError('ERROR: unexpected median: %d' % median)
    solution = []
    while heap:
        _, x = heapq.heappop(heap)
        solution.append(str(x))
    print(' '.join(solution))


if __name__ == '__main__':
    main()
