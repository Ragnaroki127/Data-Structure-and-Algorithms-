#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    tree.setdefault(0, {})
    n = 1
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if tree[current_node].get(current_symbol, False):
                current_node = tree[current_node][current_symbol]
            else:
                tree[current_node].setdefault(current_symbol, n)
                current_node = n
                if i != len(pattern) - 1:
                    tree.setdefault(current_node, {})
                n += 1    
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
