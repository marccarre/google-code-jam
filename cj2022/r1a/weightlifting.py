from typing import List
import itertools
import sys


def main() -> None:
    testcases = int(input())
    for i in range(1, testcases + 1):
        e, w = [int(x) for x in input().split()]
        workout = []
        for _ in range(e):
            weights = [int(x) for x in input().split()]
            assert len(weights) == w
            workout.append(weights)
        assert len(workout) == e
        num_ops = min_ops(workout)
        print('Case #%d: %d' % (i, num_ops))


def min_ops(workout: List[int]) -> int:    
    return 0


def count_ops(workout: List[int]) -> int:    
    min_workout = 0
    for weights in workout:
        for permutation in set(itertools.permutations(expand(weights))):
            machine = list(permutation)


def has_all_weights(target, machine):
    weights = [0] * len(target)
    for w in machine:
        weights[w] += 1
    return weights == target


def expand(weights: List[int]) -> List[int]:
    stack = []
    for i, c in enumerate(weights):
        stack.extend([i] * c)
    return stack


def permute(target, weights, machine, left=0):
    if has_all_weights(target, machine) and all(w == 0 for w in weights):
        print(machine)
    else:
        for i in range(left, len(weights)):
            if weights[i] == 0:
                continue
            print(weights, machine)
            weights[i] -= 1
            machine.append(i)
            weights[i], weights[left] = weights[left], weights[i]
            permute(target, weights, machine, left + 1)
            # backtrack:
            weights[i], weights[left] = weights[left], weights[i]
            machine.pop()
            weights[i] += 1
            '''
            if weights[i] == 0:
                continue
            machine.append(weights[i])
            weights[i] -= 1
            count = sys.maxsize
            if weights[i] == 0:
                count = min(count, permute(weights, machine, count + 1, start + 1))
            else:
                for j in range(i + 1, len(weights)):
                    weights[i], weights[j] = weights[j], weights[i]
                    count = min(count, permute(weights, machine, count + 1, start))
                    weights[i], weights[j] = weights[j], weights[i] # backtrack
                '''


if __name__ == '__main__':
    main()
