r"""http://codeforces.com/contest/474/problem/A

"""
import fileinput

inp = fileinput.input()
kb = r'''qwertyuiopasdfghjkl;zxcvbnm,./'''


def solve():
    direction = {'R': -1, 'L': 1}[next(inp).strip()]
    keys = next(inp).strip()
    sol = ''.join([kb[kb.find(k) + direction] for k in keys])
    print(sol)


if __name__ == '__main__':
    solve()
