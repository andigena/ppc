r"""http://codeforces.com/contest/474/problem/D

First try, rejected."""
import fileinput
import math

modulo = 1000000007


def nCr(n, r):
    f = math.factorial
    return int(f(n) / f(r) / f(n-r))


def solve():
    inp = fileinput.input()
    t, k = map(int, next(inp).split())
    max_b = 0
    sums = [0]*10**5
    multi_sums = [0]*10**5

    for line in inp:
        a, b = map(int, line.split())

        # calculate all the possibilities up to b if it's larger than the previously seen
        if b > max_b:
            for i in range(max_b+1, b+1):
                s = 0
                # calculate all possible sequences for a single length
                # w: number of white groups
                for w in range(1, i // k + 1):
                    reds = i - w*k
                    # multisubset calculation, where can those groups be placed?
                    s += nCr(reds+1 + w - 1, w)
                    s %= modulo
                sums[i] = s+1
                multi_sums[i] = multi_sums[i-1] + s + 1
        max_b = b

        print((multi_sums[b] - multi_sums[a-1]) % modulo)

if __name__ == '__main__':
    solve()