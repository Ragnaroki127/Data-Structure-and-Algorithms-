# python3

def MinAndMax(i, j, M, m, op):
    min_val = 100000
    max_val = -100000
    for k in range(i, j):
        if op[k] == '+':
            a = M[i][k] + M[k+1][j]
            b = M[i][k] + m[k+1][j]
            c = m[i][k] + M[k+1][j]
            d = m[i][k] + M[k+1][j]
        elif op[k] == '-':
            a = M[i][k] - M[k + 1][j]
            b = M[i][k] - m[k + 1][j]
            c = m[i][k] - M[k + 1][j]
            d = m[i][k] - M[k + 1][j]
        elif op[k] == '*':
            a = M[i][k] * M[k + 1][j]
            b = M[i][k] * m[k + 1][j]
            c = m[i][k] * M[k + 1][j]
            d = m[i][k] * M[k + 1][j]
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    nums = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    ops = [dataset[i] for i in range(1, len(dataset), 2)]
    n = len(nums)
    M = [[0 for _ in range(n)] for _ in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = nums[i]
        m[i][i] = nums[i]
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, M, m, ops)
    return M[0][n - 1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
