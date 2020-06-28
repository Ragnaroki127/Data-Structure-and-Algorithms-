# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    if len(segments) == 1:
        points.append(segments[0][1])
        return points
    segments.sort(key=(lambda x:x[1]))
    segments.sort(key=(lambda x:x[0]))
    current, last = 0, 0
    min_right = segments[0][1]
    while current < len(segments):
        if segments[current][0] > segments[last][1]:
            last = current
            points.append(min_right)
            min_right = segments[current][1]
        if segments[current][1] < min_right:
            min_right = segments[current][1]
        if current == len(segments) - 1:
            points.append(min_right)
        current += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
