from utils import puzzlefile, slurp, unpack, assert_eq, numbers
from collections import defaultdict


def middle(l):
    return l[len(l) // 2]

def part1(s):
    order, pages = unpack(s, sep="\n\n")
    order = [numbers(row) for row in unpack(order)]
    pages = [numbers(row) for row in unpack(pages)]
    O = defaultdict(list)
    for a, b in order:
        O[a].append(b)
    acc = 0
    for p in pages:
        oks = []
        for i, _ in enumerate(p):
            for c in p[i + 1:]:
                oks.append(c in O[p[i]])
        if all(oks):
            acc += middle(p)
    return acc

def part2(s):
    return 0


puzzledata = slurp(puzzlefile(__file__))
testdata1 = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|29
47|61
75|61
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

print("#--- Day x.1: <name>:", end=" ")

assert_eq(part1(testdata1), 143)
print(part1(puzzledata))

# print("#--- Day x.2: <name>:", end=" ")

# assert_eq(part2(testdata2), 0)
# print(part2(puzzledata))
