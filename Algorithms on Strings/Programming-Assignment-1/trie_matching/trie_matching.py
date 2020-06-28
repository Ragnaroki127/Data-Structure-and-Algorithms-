# python3
import sys


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

def prefix_trie_matching(text, trie):
    symbol = text[0]
    v = 0
    n = 0
    while True:
        if v not in trie: 
            return True
        elif symbol in trie[v] and n != len(text):
            v = trie[v][symbol]
            n += 1
            symbol = text[n] if n != len(text) else -1
        else:
            return False
            

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    n = 0
    while text:
        if prefix_trie_matching(text, trie):
            result.append(n)
        text = text[1:]
        n += 1
    return result

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
