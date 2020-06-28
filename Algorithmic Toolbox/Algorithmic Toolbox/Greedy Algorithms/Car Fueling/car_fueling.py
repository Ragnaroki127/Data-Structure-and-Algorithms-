# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    numRefills = 0
    currentRefill = 0
    n = len(stops)
    stops.insert(0, 0)
    stops.append(d)
    while currentRefill <= n:
        lastRefill = currentRefill
        while currentRefill <= n and stops[currentRefill + 1] - stops[lastRefill] <= m:
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            numRefills += 1
    return numRefills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
