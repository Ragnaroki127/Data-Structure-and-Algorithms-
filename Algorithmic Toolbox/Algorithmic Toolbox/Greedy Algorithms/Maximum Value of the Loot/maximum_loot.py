# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    prices_per_unit = []
    for i in range(len(weights)):
        prices_per_unit.append((prices[i] / weights[i]))
    indexes = [index for index,value in sorted(list(enumerate(prices_per_unit)),key=lambda x:x[1], reverse=True)]
    Value = 0
    for i in range(len(weights)):
        if capacity == 0:
            return Value
        else:
            a = min(weights[indexes[i]], capacity)
            Value += a * prices[indexes[i]] / weights[indexes[i]]
            capacity -= a
    return Value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
