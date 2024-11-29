import re
from contextlib import suppress
from queue import PriorityQueue, Empty


BIGNUM = 10**100


class P2d:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def pos(self):
        return (self.x, self.y)

    def __repr__(self):
        return "P2d(%d, %d)" % (self.x, self.y)


class Rect:
    def __init__(self, tl: P2d, br: P2d):
        assert_ge(br.x, tl.x)
        assert_ge(br.y, tl.y)
        self.tl = tl
        self.br = br

    def overlap(self, other):
        return not (
            self.br.x < other.tl.x
            or self.tl.x > other.br.x
            or self.br.y < other.tl.y
            or self.tl.y > other.br.y
        )

    def __repr__(self):
        return "Rect(%s, %s)" % (self.tl, self.br)


def neighbours(x, y, grid):
    """Return the coordinates and value of all neighbours of (x, y)"""
    n = set()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        with suppress(KeyError):
            n.add((x + dx, y + dy, grid[(x + dx, y + dy)]))
    return n


def nibble_to_bin(hexchar):
    return bin(int(hexchar, 16))[2:].zfill(4)


def lmap(op, array):
    return list(map(op, array))


def sign(n: int) -> int:
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def unique(lst):
    return set(lst)


def manhattan_distance(p0, p1) -> int:
    return sum(abs(a - b) for a, b in zip(p0, p1))


def unpack(data: str, sep="\n", fn=str):
    sections = data.strip().split(sep)
    return [fn(section) for section in sections]


def slurp(filename: str) -> str:
    with open(filename) as f:
        return f.read().rstrip()


def xor(a, b):
    return bool(a) ^ bool(b)


def assert_eq(a, b):
    assert a == b, "%s == %s" % (a, b)


def assert_ge(a, b):
    assert a >= b, "%s >= %s" % (a, b)


def chunks(data, size):
    """split a list into a list of lists"""
    for i in range(0, len(data), size):
        yield data[i : i + size]


def take(data, items):
    for _ in range(items):
        yield data.pop(0)


def numbers(s):
    """return all numbers in a string"""
    return lmap(int, re.findall(r"\d+", s))


def digits(s):
    """return all digits in a string"""
    return lmap(int, re.findall(r"\d", s))


def rev(s):
    """reverse a string"""
    return s[::-1]


def shortest_path(start, end, edges):
    """
    Get the path with lowest weight from start to end

    input:
        edges: edges[from][to] = weight
    return:
        list of tuples ((x, y), totalweight) excluding start in reverse order
    """
    paths = {start: (None, 0)}
    Q = PriorityQueue()
    visited = set()
    current = start
    while current != end:
        visited.add(current)
        current_weight = paths[current][1]
        for node, weight in edges[current].items():
            total = current_weight + weight
            if node not in paths:
                # first visit
                paths[node] = (current, total)
            elif total < paths[node][1]:
                # better path
                paths[node] = (current, total)
            else:
                # do nothing
                pass
            Q.put((total, node))
        try:
            _, next_ = Q.get(block=False)
            while next_ in visited:
                _, next_ = Q.get(block=False)
        except Empty:
            return []
        current = next_
    current = end
    path = []
    while current != start:
        path.append(paths[current])
        current = paths[current][0]
    return path


if __name__ == "__main__":
    # chunks
    assert_eq(["ab", "cd", "ef", "gh"], list(chunks("abcdefgh", 2)))
    assert_eq(["abcd", "efgh"], list(chunks("abcdefgh", 4)))

    # take
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert_eq([1, 2, 3], list(take(data, 3)))
    assert_eq([4, 5, 6, 7, 8, 9], list(take(data, 6)))
    assert_eq([], data)

    # numbers
    assert_eq([1, 2, 3, 4], numbers("hell1o world 2=3++++++4"))

    # rect
    r = Rect(P2d(1, 1), P2d(3, 3))
    assert r.overlap(Rect(P2d(1, 1), P2d(2, 2)))
    assert not r.overlap(Rect(P2d(4, 4), P2d(5, 5)))
    assert r.overlap(Rect(P2d(0, 1), P2d(1, 1)))
