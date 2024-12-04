from utils import puzzlefile, slurp, assert_eq, parse_grid, line, cat
from contextlib import suppress


def part1(s):
    G, XMAX, YMAX = parse_grid(s)
    words = []
    for x, y in [(x, y) for x, y in G if G[(x, y)] == "X"]:
        for heading in ["E", "NE", "N", "NW", "W", "SW", "S", "SE"]:
            with suppress(KeyError):
                words.append(cat(G[(xx, yy)] for xx, yy in line(x, y, heading, 4)))
    return words.count("XMAS")


def part2(s):
    G, XMAX, YMAX = parse_grid(s)
    acc = 0
    for x, y in [(x, y) for x, y in G if G[(x, y)] == "A"]:
        with suppress(KeyError):
            words = [
                G[(x - 1, y - 1)] + G[(x, y)] + G[(x + 1, y + 1)],
                G[(x + 1, y - 1)] + G[(x, y)] + G[(x - 1, y + 1)],
                G[(x - 1, y + 1)] + G[(x, y)] + G[(x + 1, y - 1)],
                G[(x + 1, y + 1)] + G[(x, y)] + G[(x - 1, y - 1)],
            ]
            acc += 1 if words.count("MAS") == 2 else 0
    return acc


puzzledata = slurp(puzzlefile(__file__))
testdata = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

print("#--- Day 4.1: Ceres Search:", end=" ")

assert_eq(part1(testdata), 18)
print(part1(puzzledata))

print("#--- Day 4.2: Ceres Search:", end=" ")

assert_eq(part2(testdata), 9)
print(part2(puzzledata))
