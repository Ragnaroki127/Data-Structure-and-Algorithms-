# python3

from itertools import combinations
import math

def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    a_sorted, num_of_inverses = merge_sort(a)
    return num_of_inverses

def merge_sort(a):
    num_of_inverses = 0
    if len(a) == 1:
        return a, num_of_inverses
    m = math.floor(len(a) / 2) - 1
    B, num_left = merge_sort(a[0:m+1])
    C, num_right = merge_sort(a[m+1:len(a)])
    a_merged, num_merged = merge(B, C)
    num_of_inverses += num_left + num_right + num_merged
    return a_merged, num_of_inverses

def merge(left, right):
    num_of_inverses = 0
    merged_list = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged_list.append((left[0]))
            left.pop(0)
        else:
            merged_list.append((right[0]))
            right.pop(0)
            num_of_inverses += len(left)
    if len(left) == 0:
        for i in range(0, len(right)):
            merged_list.append(right[i])
    elif len(right) == 0:
        for i in range(0, len(left)):
            merged_list.append(left[i])

    return merged_list, num_of_inverses

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
