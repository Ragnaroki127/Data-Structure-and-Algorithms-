# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_better(num1, num2):
    return (int(str(num1) + str(num2)) > int(str(num2) + str(num1)))

def largest_number(numbers):
    max = ''
    while len(numbers) > 1:
        best_num = numbers[0]
        best_ind = 0
        for i in range(len(numbers)):
            if is_better(numbers[i], best_num):
                best_num = numbers[i]
                best_ind = i
        max += str(best_num)
        del numbers[best_ind]
    max += str(numbers[0])
    return int(max)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
