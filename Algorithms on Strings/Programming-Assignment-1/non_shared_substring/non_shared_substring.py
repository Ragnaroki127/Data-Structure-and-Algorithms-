# python3
import sys
sys.setrecursionlimit(1000000)

class Node():
    def __init__(self, start_ind, length, node_id):
        self.start_ind = start_ind
        self.length = length
        self.node_id = node_id
        self.children = []

def add_node_to_tree(current_node, i, text):
    flag = 1
    for sub_node in current_node.children:
        k = 0
        if len(text[i:]) > sub_node.length:
            while k < sub_node.length:
                if text[sub_node.start_ind:][k] != text[i:][k]:
                    break
                k += 1
            if k == 0:
                continue               
            elif k == sub_node.length:
                add_node_to_tree(sub_node, i + sub_node.length, text)
                flag = 0
            else:
                flag = 0
                temp_children = sub_node.children
                
                sub_node.children = [Node(sub_node.start_ind + k, sub_node.length - k, 1)]
                sub_node.length = k
                sub_node.children[0].children = temp_children
                add_node_to_tree(sub_node, i + k, text)
        else:
            while k < len(text[i:]):
                if text[sub_node.start_ind:][k] != text[i:][k]:
                    break
                k += 1
            if k == 0:
                continue
            elif k == len(text[i:]):
                return
            else:
                flag = 0
                temp_children = sub_node.children
                sub_node.children = [Node(sub_node.start_ind + k, sub_node.length - k, 1)]
                sub_node.length = k
                sub_node.children[0].children = temp_children
                add_node_to_tree(sub_node, i + k, text)
    if flag:
        current_node.children.append(Node(i, len(text[i:]), 1))


def cat_to_result(node, text, result):
    if node.node_id != 0:
        result.append(text[node.start_ind:node.start_ind + node.length])
    for sub_node in node.children:
        cat_to_result(sub_node, text, result)


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    trie_root = Node(-1, -1, 0)
    for i in range(len(text)):
        current_node = trie_root
        add_node_to_tree(current_node, i, text)
    cat_to_result(trie_root, text, result)            
    return result


def solve (p, q):
    l = len(p)
    m = len(q)
    for i in range(min(l, m)):
        for j in range(l-i):
            s = p[j:j+i+1]
            if not s in q:
                return s
    return


p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')
'''
if __name__ == '__main__':
	p = 'CCAAGC'
	q = 'CATGCT'
	text = p + '#' + q + '$'
	result = build_suffix_tree(text)
	print('\n'.join(result))
'''