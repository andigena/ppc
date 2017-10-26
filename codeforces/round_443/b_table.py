import fileinput

inp = fileinput.input()


def solve():
    n, k = map(int, next(inp).strip().split())
    powers = [int(x) for x in next(inp).strip().split()]
    wc = 0
    for _ in range(n*2):
        p = powers[0]
        if p > powers[1]:
            powers.append(powers.pop(1))
            wc += 1
            if wc >= k:
                print(p)
                break
        else:
            powers.append(powers.pop(0))
            wc = 1
    else:
        print(n)


if __name__ == '__main__':
    solve()
