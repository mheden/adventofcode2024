from utils import puzzlefile, slurp, unpack, assert_eq, numbers


def is_safe(V):
    inc = True
    dec = True
    diff = True
    prev = V[0]
    for curr in V[1:]:
        inc = inc and (prev < curr)
        dec = dec and (prev > curr)
        diff = diff and (abs(prev - curr) >= 1 and abs(prev - curr) <= 3)
        prev = curr
    return (inc or dec) and diff


def part1(s):
    acc = 0
    for report in unpack(s):
        V = numbers(report)
        acc += 1 if is_safe(V) else 0
    return acc


def permutate(report):
    reports = []
    for i, _ in enumerate(report):
        reports.append(report[:i] + report[i + 1 :])
    return reports


def part2(s):
    acc = 0
    for report in unpack(s):
        V = numbers(report)
        if is_safe(V):
            acc += 1
        else:
            acc += 1 if any(map(is_safe, permutate(V))) else 0
    return acc


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
