import fileinput

inp = fileinput.input()


def solve():
    n = int(next(inp))
    curr_day = 0
    for i in range(n):
        s, d = map(int, next(inp).strip().split())
        if curr_day < s:
            curr_day = s
        else:
            t = curr_day + 1 - s
            t = ((t + d - 1) // d) * d
            curr_day = s + t

    print(curr_day)


if __name__ == '__main__':
    solve()
