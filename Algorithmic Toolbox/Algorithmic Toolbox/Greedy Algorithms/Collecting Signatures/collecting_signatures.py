# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    points = []
    segments.sort(key = (lambda x:x[1]))
    point = segments[0][1]
    points.append(point)
    for i in range(len(segments)):
        if point < segments[i][0] or point > segments[i][1]:
            point = segments[i][1]
            points.append(point)
    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
