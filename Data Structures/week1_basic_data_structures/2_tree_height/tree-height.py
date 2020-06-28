# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
        def __init__(self, label):
                self.val = label
                self.child = []

class TreeHeight:

        nodes = []
        root = -1
        n = -1
        parent = []

        def read(self):
                self.n = int(input())
                self.parent = list(map(int, input().split()))

        def init_tree(self):
                # Replace this code with a faster implementation
                for i in range(self.n):
                        self.nodes.append(Node(i))
                for child_index in range(self.n):
                        parent_index = self.parent[child_index]
                        if parent_index == -1:
                                self.root = child_index
                        else:
                                self.nodes[parent_index].child.append(child_index)

        def compute_height(self, ind):
                if len(self.nodes[ind].child) == 0:
                        return 1
                return 1 + max([self.compute_height(i) for i in self.nodes[ind].child])


def main():
  tree = TreeHeight()
  tree.read()
  tree.init_tree()
  print(tree.compute_height(tree.root))

threading.Thread(target=main).start()
