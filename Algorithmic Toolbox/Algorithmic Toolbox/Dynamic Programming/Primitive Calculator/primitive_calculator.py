# python3
class element:
    def __init__(self, opts, intermediates):
        self.num_ops = opts
        self.intermediates = intermediates

def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    min_num_operations = [element(0, [])]
    operations = ['multiply_3', 'multiply_2', 'add_1']
    for i in range(1, n):
        min_num_operations.append(element(1000000, []))
        for opt in operations:
            if opt == 'multiply_3':
                if (i + 1) % 3 == 0:
                    num_opts = min_num_operations[int((i + 1) / 3 - 1)].num_ops + 1
                    if num_opts < min_num_operations[i].num_ops:
                        min_num_operations[i].num_ops = num_opts
                        min_num_operations[i].intermediates = min_num_operations[int((i + 1) / 3 - 1)].intermediates[:]
                        min_num_operations[i].intermediates.append(int((i + 1) / 3))
            if opt == 'multiply_2':
                if (i + 1) % 2 == 0:
                    num_opts = min_num_operations[int((i + 1) / 2 - 1)].num_ops + 1
                    if num_opts < min_num_operations[i].num_ops:
                        min_num_operations[i].num_ops = num_opts
                        min_num_operations[i].intermediates = min_num_operations[int((i + 1) / 2 - 1)].intermediates[:]
                        min_num_operations[i].intermediates.append(int((i + 1) / 2))
            elif opt == 'add_1':
                num_opts = min_num_operations[i - 1].num_ops + 1
                if num_opts < min_num_operations[i].num_ops:
                    min_num_operations[i].num_ops = num_opts
                    min_num_operations[i].intermediates = min_num_operations[i - 1].intermediates[:]
                    min_num_operations[i].intermediates.append(i)
    min_num_operations[n - 1].intermediates.append(n)
    return min_num_operations[n - 1].intermediates


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
