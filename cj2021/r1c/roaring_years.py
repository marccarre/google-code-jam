'''
$ python cj2021/r1c/roaring_years.py < tests/cj2021/r1c/roaring_years.txt
Case #1: 2021
Case #2: 2122
Case #3: 78910
Case #4: 123

'''

from typing import List, Tuple


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        y = int(input())
        next_y = next_year(y)
        print('Case #%d: %s' % (i, next_y))


def next_year(y: int) -> int:
    while True:
        y = int(y)
        y += 1
        y = str(y)
        for chunk_size in range(1, 1 + len(y) // 2):
            chunks = _chunks(y, chunk_size)
            if all(int(chunks[i]) == int(chunks[i - 1]) + 1 for i in range(1, len(chunks))):
                return int(y)


def _chunks(y: str, chunk_size: int) -> List[int]:
    chunks = []
    i = 0
    while i < len(y):
        chunk = y[i:i + chunk_size]
        chunks.append(chunk)
        i += chunk_size
        if chunk == '9' * len(chunk):
            chunk_size += 1
    return chunks


if __name__ == '__main__':
    main()
