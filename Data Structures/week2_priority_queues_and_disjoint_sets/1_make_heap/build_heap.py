# python3

def parent(i):
        return int((i + 1) / 2 - 1)

def left_child(i):
        return 2 * i + 1

def right_child(i):
        return 2 * i + 2

class Heap:
    def __init__(self, input_array):
        self.max_size = 1e6
        self.heap = input_array
        self.heap_size = len(input_array)
        self.swaps = []

    def sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[parent(i)]:
            self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
            self.swaps.append((i, parent(i)))
            i = parent(i)

    def sift_down(self, i):
        min_index = i
        l = left_child(i)
        if l < self.heap_size and self.heap[min_index] > self.heap[l]:
            min_index = l
        r = right_child(i)
        if r < self.heap_size and self.heap[min_index] > self.heap[r]:
            min_index = r
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.swaps.append((i, min_index))
            self.sift_down(min_index)

    def build_heap(self):
        for i in range(int(self.heap_size / 2 - 1), -1, -1):
            self.sift_down(i)

    def insert(self, p):
        if self.heap_size == self.max_size:
            raise('ERROR')
        self.heap_size += 1
        self.heap[self.heap_size - 1] = p
        self.sift_up(self.heap_size - 1)

    def extract_max(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.sift_down(0)
        return result


    


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    heap = Heap(data)
    heap.build_heap()
    return heap.swaps, heap.heap


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps, heap = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
