# python3
import math

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def get_frequency(nums, element):
    count = 0
    for i in range(len(nums)):
        if nums[i] == element:
            count += 1
    return count

def get_majority_element(elements):
    if (len(elements) == 1): return elements[0]
    k = math.floor(len(elements) / 2.)
    lsub = get_majority_element(elements[0:k])
    rsub = get_majority_element(elements[k:len(elements)])
    if lsub == rsub:
        return lsub
    lcount = get_frequency(elements, lsub)
    rcount = get_frequency(elements, rsub)
    if lcount != 'NO RESULT' and lcount > k:
        return lsub
    elif rcount != 'NO RESULT' and rcount > k:
        return rsub
    else:
        return 'NO RESULT'

def majority_element(elements):
    if get_majority_element(elements) == 'NO RESULT':
        return 0
    else:
        return 1


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
    #print(get_majority_element(input_elements))
