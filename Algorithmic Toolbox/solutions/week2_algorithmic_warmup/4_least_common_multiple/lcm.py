# Uses python3
import sys

def gcd(a, b):
    result = 0
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a >= b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(int((a / gcd(a, b)) * (b / gcd(a, b)) * gcd(a, b)))

