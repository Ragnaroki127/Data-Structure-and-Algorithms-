#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if tree == []: return True
  result = []
  inorder_recur(tree, 0, result)
  for i in range(0, result.index(tree[0][0])):
    if result[i] >= result[i + 1]:
      return False
  for i in range(result.index(tree[0][0]), len(result) - 1):
    if result[i] > result[i + 1]:
      return False
  return True


def inorder_recur(tree, ind, result):
  if ind == -1:
    return
  inorder_recur(tree, tree[ind][1], result)
  result.append(tree[ind][0])
  inorder_recur(tree, tree[ind][2], result)


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
