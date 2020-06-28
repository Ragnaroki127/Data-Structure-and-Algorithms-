# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    self.root_ind = 0
    self.inorder_recur(self.root_ind)
    # Finish the implementation
    # You may need to add a new recursive method to do that      
    return self.result

  def inorder_recur(self, ind):
    if ind == -1:
      return
    self.inorder_recur(self.left[ind])
    self.result.append(self.key[ind])
    self.inorder_recur(self.right[ind])

  def preOrder(self):
    self.result = []
    self.root_ind = 0
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preorder_recur(self.root_ind)
    return self.result

  def preorder_recur(self, ind):
    if ind == -1:
      return
    self.result.append(self.key[ind])
    self.preorder_recur(self.left[ind])
    self.preorder_recur(self.right[ind])

  def postOrder(self):
    self.result = []
    self.root_ind = 0
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postorder_recur(self.root_ind)            
    return self.result

  def postorder_recur(self, ind):
    if ind == -1:
      return 
    self.postorder_recur(self.left[ind])
    self.postorder_recur(self.right[ind])
    self.result.append(self.key[ind])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
