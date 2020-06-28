#!/usr/bin/python3

import sys, threading
#import numpy as np

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if tree == []:
    return True
  return is_binary_util(tree, 0, float('-inf'), float('inf'))
  
def is_binary_util(tree, ind, min_val, max_val):
  if ind == -1:
    return True
  if tree[ind][0] < min_val or tree[ind][0] >= max_val:
    return False
  return is_binary_util(tree, tree[ind][1], min_val, tree[ind][0]) and is_binary_util(tree, tree[ind][2], tree[ind][0], max_val)

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
