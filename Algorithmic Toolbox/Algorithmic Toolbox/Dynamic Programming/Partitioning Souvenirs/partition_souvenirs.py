# python3

from itertools import product
from sys import stdin

'''
def maximum_gold(capacity, weights):
    gold_weight = [[0 for i in range(capacity + 1)] for i in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for w in range(1, capacity + 1):
            gold_weight[i][w] = gold_weight[i - 1][w]
            if weights[i - 1] <= w:
                val = gold_weight[i - 1][w - weights[i - 1]] + weights[i - 1]
                if val > gold_weight[i][w]:
                    gold_weight[i][w] = val
    weight_indexes = []
    weight = capacity
    element = len(weights)
    for i in range(len(weights)):
        if gold_weight[element][weight] >= weights[element - 1]:
            if gold_weight[element][weight] == gold_weight[element - 1][weight - weights[element - 1]] + weights[element - 1]:
                weight_indexes.append(element - 1)
                weight -= weights[element - 1]
        element -= 1
    return gold_weight[len(weights)][capacity], weight_indexes

def partition3(values):
    #assert 1 <= len(values) <= 20
    #assert all(1 <= v <= 30 for v in values)

    sum_values = sum(values)
    if (sum_values / 3) % 1 != 0 or len(values) < 3:
        return 0
    else:
        max1, indexes1 = maximum_gold(int(sum_values / 3 * 2), values)
        if max1 != int(sum_values / 3 * 2):
            return 0
        else:
            values = [values[i] for i in range(len(values)) if i in indexes1]
            max2, indexes2 = maximum_gold(int(sum_values/3), values)
            if max2 != int(sum_values/3):
                return 0
            else:
                return 1
'''


def partition3(values):
    total = sum(values)
    if len(values) < 3 or total % 3:  # 1
        return 0
    third = total // 3
    table = [[0] * (len(values) + 1) for _ in range(third + 1)]  # 2

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):  # 3
            ii = i - values[j - 1]  # 4
            if values[j - 1] == i or (ii > 0 and table[ii][j - 1]):  # 5
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]  # 6

    return 1 if table[-1][-1] == 2 else 0

if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    #print(input_n, input_values)
    print(partition3(input_values))
