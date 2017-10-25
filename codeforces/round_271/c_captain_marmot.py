r""" http://codeforces.com/contest/474/problem/C

Some basic vector trickery and brute forcing involved. Only passes the submission tests when run under PyPy 3, timeouts
otherwise.
"""
import collections
import fileinput
import itertools

inp = fileinput.input()

Vect = collections.namedtuple('Vect', ('x', 'y'))
Mole = collections.namedtuple('Mole', ('pos', 'home'))

nullvect = Vect(0, 0)


def subtract(v1, v2):
    return Vect(v2.x - v1.x, v2.y - v1.y)


def add(v1, v2):
    return Vect(v1.x + v2.x, v1.y + v2.y)


def distance_squared(v1, v2):
    r""" Returns the distance without calculating the square root to speed it up, avoid floats."""
    d = subtract(v1, v2)
    l = d.x**2 + d.y**2
    return l


def rotate_cw(m):
    return Vect(m.y, -m.x)


def rotate_ccw(m):
    return Vect(-m.y, m.x)


def move(m, times=1):
    tv = subtract(m.home, m.pos)
    for _ in range(times):
        tv = rotate_ccw(tv)
    return Mole(add(m.home, tv), m.home)


def is_compact(regiment):
    for i in range(3):
        r = regiment[:3]
        m = r.pop(i)
        d1 = subtract(m.pos, r[0].pos)
        d2 = subtract(m.pos, r[1].pos)
        if d1 == nullvect or d2 == nullvect:
            return False

        if rotate_ccw(d1) == d2 or rotate_cw(d1) == d2:
            m4_pos = add(m.pos, d1)
            m4_pos = add(m4_pos, d2)
            if m4_pos == regiment[3].pos:
                return True

    return False


def brute(regiment):
    min_moves = 2**32
    for moves in itertools.product(range(4), repeat=4):
        move_count = sum(moves)
        if move_count >= min_moves:
            continue

        reg = [move(regiment[idx], moves[idx]) for idx in range(len(moves))]
        if is_compact(reg):
            min_moves = move_count

    if min_moves < 2**32:
        return min_moves
    else:
        return -1


def solve():
    n = int(next(inp))
    regiments = [[None]*4 for _ in range(n)]
    for i in range(n):
        for ridx, line in enumerate(itertools.islice(inp, 0, 4)):
            coords = [int(i) for i in line.strip().split()]
            pos = Vect(coords[0], coords[1])
            home = Vect(coords[2], coords[3])
            regiments[i][ridx] = Mole(pos, home)

        res = brute(regiments[i])
        print(res)


if __name__ == '__main__':
    solve()
