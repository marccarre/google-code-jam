from typing import List, Optional, Tuple
from sys import maxsize


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        cartridges = []
        for _ in range(3):
            c, m, y, k = [int(x) for x in input().split()]
            cartridges.append((c, m, y, k))
        solution = colour(cartridges)
        if solution is None:
            print('Case #%d: IMPOSSIBLE' % (i))
        else:
            c, m, y, k = solution
            print('Case #%d: %d %d %d %d' % (i, c, m, y, k))


NUM_COLOURS = 4
INK_FOR_D = 1_000_000


def colour(cartridges: List[Tuple[int, int, int, int]]) -> Optional[Tuple[int, int, int, int]]:
    min_ink = [maxsize, maxsize, maxsize, maxsize]
    for cartridge in cartridges:
        for i in range(NUM_COLOURS):
            min_ink[i] = min(min_ink[i], cartridge[i])
    if sum(min_ink) < INK_FOR_D:
        return None
    else:
        s = 0
        used_ink = [0, 0, 0, 0]
        for i, ink in enumerate(min_ink):
            used = min(INK_FOR_D - s, ink)
            used_ink[i] = used
            s += used
        assert(sum(used_ink) == INK_FOR_D)
        return tuple(used_ink)


if __name__ == '__main__':
    main()
