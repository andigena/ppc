r"""http://codeforces.com/contest/474/problem/B

Calculate running total while reading the pile sizes, then do a binary search for every label."""
import bisect
import fileinput

inp = fileinput.input()


def solve():
    n = int(next(inp))
    piles = [0]*(n+1)
    for idx, i in enumerate(map(int, next(inp).split()), 1):
        piles[idx] = piles[idx-1] + i

    _ = int(next(inp))
    for l in map(int, next(inp).split()):
        p = bisect.bisect_left(piles, l)
        print(p)


if __name__ == '__main__':
    solve()
