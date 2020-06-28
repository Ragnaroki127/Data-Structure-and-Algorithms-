# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])
        return result[n]

n = int(input())
print(calc_fib(n))
