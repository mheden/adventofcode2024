from utils import slurp, unpack, assert_eq
import re


def part1(s):
    acc = 0
    for line in unpack(s):
        for m in re.findall(r"mul\((\d+),(\d+)\)", line):
            acc += int(m[0]) * int(m[1])
    return acc


def part2(s):
    acc = 0
    enable = True
    for line in unpack(s):
        for m in re.findall(r"(don't|do|mul)(\((\d+),(\d+)\))?", line):
            if m[0] == "mul" and m[2] and enable:
                acc += int(m[2]) * int(m[3])
            elif m[0] == "don't":
                enable = False
            elif m[0] == "do":
                enable = True
    return acc


filedata = slurp("03.txt")
testdata1 = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
testdata2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


print("#--- Day 3.1: Mull It Over:", end=" ")

assert_eq(part1(testdata1), 161)
print(part1(filedata))

print("#--- Day 3.2: Mull It Over:", end=" ")

assert_eq(part2(testdata2), 48)
print(part2(filedata))
