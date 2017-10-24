r"""http://codeforces.com/contest/474/problem/D

Using memoization + recursion, rejected with timeout."""
import fileinput

modulo = 1000000007
inp = fileinput.input()
memo = {}


def DP_memoized(k, n):
    if n == 0:
        # base case
        return 1
    if (k, n) in memo:
        return memo[(k, n)]

    s = 0
    if n >= k:
        s += DP_memoized(k, n - k)
    if n >= 1:
        s += DP_memoized(k, n - 1)

    s %= modulo
    memo[(k, n)] = s
    return s


def solve():
    t, k = map(int, next(inp).split())
    max_b = 0
    sums = [0]*10**5
    multi_sums = [0]*10**5

    for line in inp:
        a, b = map(int, line.split())

        # calculate all the possibilities up to b if it's larger than the previously seen
        if b > max_b:
            for i in range(max_b+1, b+1):
                s = DP_memoized(k, i)
                sums[i] = s
                multi_sums[i] = multi_sums[i-1] + s
        max_b = b

        print((multi_sums[b] - multi_sums[a-1]) % modulo)

if __name__ == '__main__':
    solve()