from typing import List


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        s = first_string(input())
        print('Case #%d: %s' % (i, s))


def first_string(s: str) -> str:
    first = []
    for i in range(len(s)):
        first.append(s[i])
        # Look ahead:
        dup = False
        for j in range(i + 1, len(s)):
            if s[i] < s[j]:
                dup = True
            if s[i] > s[j]:
                break
        if dup:
            first.append(s[i])
    return ''.join(first)


if __name__ == '__main__':
    main()
