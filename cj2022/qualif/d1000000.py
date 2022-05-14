from typing import List


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        num_dices = int(input())
        dices = [int(x) for x in input().split()]
        assert len(dices) == num_dices
        length = longest_straight(dices)
        print('Case #%d: %d' % (i, length))


def longest_straight(dices: List[int]) -> int:
    dices.sort()
    value = 1
    longest = 0
    for dice in dices:
        if value <= dice:
            longest += 1
            value += 1
    return longest


if __name__ == '__main__':
    main()
