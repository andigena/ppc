r"""http://codeforces.com/contest/474/problem/D

Only this version is fast enough to be accepted."""
import fileinput

modulo = 1000000007
upper_limit = 10**5 + 1
inp = fileinput.input()


def solve():
    t, k = map(int, next(inp).split())
    # the running total of the possibilites to ease calculating intervals
    rtotal = [0]*(upper_limit + 1)
    rtotal[0] = 0
    rtotal[1] = 1
    for i in range(1, upper_limit):
        s = rtotal[i]-rtotal[i-1] + (rtotal[i-k+1]-rtotal[i-k] if i >= k else 0)
        rtotal[i+1] = (rtotal[i] + s) % modulo
        if rtotal[i+1] < 0:
            pass

    for line in inp:
        a, b = map(int, line.split())
        print((rtotal[b+1] - rtotal[a]) % modulo)

if __name__ == '__main__':
    solve()
