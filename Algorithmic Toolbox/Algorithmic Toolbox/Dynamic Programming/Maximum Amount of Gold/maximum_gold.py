# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    gold_weight = [[0 for i in range(capacity + 1)] for i in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for w in range(1, capacity + 1):
            gold_weight[i][w] = gold_weight[i - 1][w]
            if weights[i - 1] <= w:
                val = gold_weight[i - 1][w - weights[i - 1]] + weights[i - 1]
                if val > gold_weight[i][w]:
                    gold_weight[i][w] = val
    weight_indexes = []
    for i in range(len(weights)):
        if gold_weight[len(weights) - i][capacity] == gold_weight[len(weights)][capacity]:
            weight_indexes.append(compute_path(len(weights) - i, capacity, gold_weight, weights))
    return gold_weight[len(weights)][capacity], weight_indexes

def compute_path(element, weight, gold_weight, weights):
    weight_indexes = []
    for i in range(len(weights)):
        if gold_weight[element][weight] >= weights[element - 1]:
            if gold_weight[element][weight] == gold_weight[element - 1][weight - weights[element - 1]] + weights[element - 1]:
                weight_indexes.append(element - 1)
                weight -= weights[element - 1]
        element -= 1
    return weight_indexes


if __name__ == '__main__':
    input_capacity, n = list(map(int, input().split()))
    input_weights = list(map(int, input().split()))

    #input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    #assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
