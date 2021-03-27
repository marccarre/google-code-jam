from typing import List


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        x, y, s = input().split()
        x = int(x)
        y = int(y)
        out = mau(x, y, s)
        print('Case #%d: %s' % (i, out))


FIXED, C, J = 0, 1, 2


def mau(x: int, y: int, s: str) -> int:
    s = list(s)
    costs = [[0, 0, 0] for _ in range(len(s))]
    for i in range(1, len(s)):
        if s[i] == 'C':
            if s[i-1] == 'C':
                costs[i][FIXED] = costs[i-1][FIXED]
            elif s[i-1] == 'J':
                costs[i][FIXED] = costs[i-1][FIXED] + y
            else:
                costs[i][FIXED] = min(costs[i-1][C], costs[i-1][J] + y)
        elif s[i] == 'J':
            if s[i-1] == 'C':
                costs[i][FIXED] = costs[i-1][FIXED] + x
            elif s[i-1] == 'J':
                costs[i][FIXED] = costs[i-1][FIXED]
            else:
                costs[i][FIXED] = min(costs[i-1][C] + x, costs[i-1][J])
        else:
            if s[i-1] == 'C':
                costs[i][J] = costs[i-1][FIXED] + x
                costs[i][C] = costs[i-1][FIXED]
            elif s[i-1] == 'J':
                costs[i][J] = costs[i-1][FIXED]
                costs[i][C] = costs[i-1][FIXED] + y
            else:
                costs[i][J] = min(costs[i-1][C] + x, costs[i-1][J])
                costs[i][C] = min(costs[i-1][C], costs[i-1][J] + y)
    return costs[-1][FIXED] if s[-1] != '?' else min(costs[-1][C], costs[-1][J])


def mau_greedy(x: int, y: int, s: str) -> int:
    def costs_for(s: List[str]) -> int:
        costs = 0
        for i in range(len(s) - 1):
            if s[i] == 'C':
                if s[i + 1] == 'J':
                    costs += x
                elif s[i + 1] == '?':
                    s[i + 1] = 'C'
            elif s[i] == 'J':
                if s[i + 1] == 'C':
                    costs += y
                elif s[i + 1] == '?':
                    s[i + 1] = 'J'
        return costs
    if s[0] == '?':
        return min(costs_for(list('C' + s[1:])), costs_for(list('F' + s[1:])))
    return costs_for(list(s))


if __name__ == '__main__':
    main()
