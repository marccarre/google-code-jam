'''
python cj2021/r1a/append_sort.py < tests/cj2021/r1a/append_sort.txt
'''

from typing import List, Tuple


DEBUG = False


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        n = int(input())
        nums = [int(x) for x in input().split()]
        count, _ = num_ops(nums)
        print('Case #%d: %s' % (i, count))


def num_ops(nums: List[int]) -> Tuple[int,  List[int]]:
    if DEBUG:
        print(nums)
    count = 0
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            if DEBUG:
                print(nums)
            a, b = str(nums[i - 1]), str(nums[i])
            if len(a) == len(b):
                nums[i] *= 10
                count += 1
            else:
                k = len(a) - len(b)
                nums[i] *= 10 ** k
                count += k
                if nums[i - 1] >= nums[i]:
                    if a.startswith(b) and a[-1] != '9':
                        nums[i] = nums[i - 1] + 1
                    else:
                        nums[i] *= 10
                        count += 1
    if DEBUG:
        print(nums)
    return count, nums


if __name__ == '__main__':
    main()
