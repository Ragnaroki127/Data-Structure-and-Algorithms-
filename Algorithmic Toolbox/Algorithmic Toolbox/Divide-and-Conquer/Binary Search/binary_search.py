# python3
import math

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, low, high, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4

    if (high < low): return -1
    mid = low + math.floor((high - low) / 2.)
    if query == keys[mid]:
        return mid
    elif query > keys[mid]:
        return binary_search(keys, mid + 1, high, query)
    else:
        return binary_search(keys, low, mid - 1, query)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, 0, len(input_keys) - 1, q), end=' ')
