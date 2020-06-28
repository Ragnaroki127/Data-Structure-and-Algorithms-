# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append((fib[i - 1] + fib[i - 2]) % 10)
        return fib[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
