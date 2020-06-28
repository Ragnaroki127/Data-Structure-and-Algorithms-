# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n
    else:
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])
        return result[n]

def get_fibonacci_huge(n, m):
    iters = 0
    mods = []
    for i in range(n + 1):
        mods.append(calc_fib(i) % m)
        if calc_fib(i + 1) % m == 0 and calc_fib(i + 2) % m == 1:
            iters = i + 1
            break
        if i == n:
            iters = n + 1
    return mods[n % iters]


if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
