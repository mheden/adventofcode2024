from utils import puzzlefile, slurp, unpack, assert_eq, numbers


def is_safe(report):
    inc = True
    dec = True
    diff = True
    prev = report[0]
    for curr in report[1:]:
        inc = inc and (prev < curr)
        dec = dec and (prev > curr)
        diff = diff and (abs(prev - curr) >= 1 and abs(prev - curr) <= 3)
        prev = curr
    return (inc or dec) and diff


def part1(s):
    return sum(is_safe(report) for report in map(numbers, unpack(s)))


def permutate(report):
    for i, _ in enumerate(report):
        yield report[:i] + report[i + 1 :]


def part2(s):
    return sum(
        is_safe(report) or any(map(is_safe, permutate(report)))
        for report in map(numbers, unpack(s))
    )


puzzledata = slurp(puzzlefile(__file__))
testdata = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

print("#--- Day 2.1: Red-Nosed Reports:", end=" ")

assert_eq(part1(testdata), 2)
print(part1(puzzledata))

print("#--- Day 2.2: Red-Nosed Reports:", end=" ")

assert_eq(part2(testdata), 4)
print(part2(puzzledata))
