from utils import slurp, unpack, assert_eq, numbers, transpose
from collections import Counter


def part1(s):
    M = [numbers(row) for row in unpack(s)]
    T = transpose(M)
    LEFT = sorted(T[0])
    RIGHT = sorted(T[1])
    return sum(abs(x - y) for x, y in zip(LEFT, RIGHT))


def part2(s):
    M = [numbers(row) for row in unpack(s)]
    T = transpose(M)
    COUNT = Counter(T[1])

    acc = 0
    for x in T[0]:
        acc += x * COUNT[x]
    return acc


filedata = slurp("01.txt")
testdata = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

print("#--- Day 1.1: Historian Hysteria:", end=" ")

assert_eq(part1(testdata), 11)
print(part1(filedata))

print("#--- Day 1.2: Historian Hysteria:", end=" ")

assert_eq(part2(testdata), 31)
print(part2(filedata))
