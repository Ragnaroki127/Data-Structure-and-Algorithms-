# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def parent(i):
        return int((i + 1) / 2 - 1)

def left_child(i):
        return 2 * i + 1

def right_child(i):
        return 2 * i + 2

class Heap:
    def __init__(self, input_array):
        self.max_size = 1e10
        self.heap = input_array
        self.heap_size = len(input_array)
        self.swaps = []

    def sift_up(self, i):
        while i > 0 and self.heap[i][1] <= self.heap[parent(i)][1]:
            if self.heap[i][1] == self.heap[parent(i)][1]:
                if self.heap[i][0] < self.heap[parent(i)][0]:
                    self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
                    i = parent(i)
                    continue
                else:
                    i = parent(i)
                    continue
            self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
            self.swaps.append((i, parent(i)))
            i = parent(i)

    def sift_down(self, i):
        min_index = i
        l = left_child(i)
        if l < self.heap_size and self.heap[min_index][1] >= self.heap[l][1]:
            if self.heap[min_index][1] == self.heap[l][1]:
                if self.heap[min_index][0] > self.heap[l][0]:
                    min_index = l
            else:
                min_index = l
        r = right_child(i)
        if r < self.heap_size and self.heap[min_index][1] >= self.heap[r][1]:
            if self.heap[min_index][1] == self.heap[r][1]:
                if self.heap[min_index][0] > self.heap[r][0]:
                    min_index = r
            else:
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

    def extract_min(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.sift_down(0)
        return result


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    '''
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result
    '''
    result = []
    data = [[x, 0] for x in range(n_workers)]
    job_queue = Heap(data)
    for job in jobs:
        current_cond = job_queue.extract_min()
        result.append(current_cond)
        new_cond = [0] * 2
        new_cond[0] = current_cond[0]
        new_cond[1] = current_cond[1] + job
        job_queue.insert(new_cond)
    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
