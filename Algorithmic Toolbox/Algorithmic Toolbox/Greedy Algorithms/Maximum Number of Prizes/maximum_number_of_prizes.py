# python3

def sum(n):
    return int(n * (n + 1) / 2)

def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    for i in range(1, n + 1):
        if sum(i+1) <= n:
            summands.append(i)
        elif sum(i) == n:
            summands.append(i)
            break
        else:
            summands.append(n - sum(i - 1))
            break

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
