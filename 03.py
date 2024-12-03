from utils import puzzlefile, slurp, unpack, assert_eq
import re


def part1(s):
    acc = 0
    for line in unpack(s):
        for a, b in re.findall(r"mul\((\d+),(\d+)\)", line):
            acc += int(a) * int(b)
    return acc


def part2(s):
    acc = 0
    enable = True
    for line in unpack(s):
        for op, a, b in re.findall(r"(don't|do|mul)(?:\((\d+),(\d+)\))?", line):
            if op == "mul" and a and enable:
                acc += int(a) * int(b)
            elif op == "don't":
                enable = False
            elif op == "do":
                enable = True
    return acc


puzzledata = slurp(puzzlefile(__file__))
testdata1 = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
testdata2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


print("#--- Day 3.1: Mull It Over:", end=" ")

assert_eq(part1(testdata1), 161)
print(part1(puzzledata))

print("#--- Day 3.2: Mull It Over:", end=" ")

assert_eq(part2(testdata2), 48)
print(part2(puzzledata))
