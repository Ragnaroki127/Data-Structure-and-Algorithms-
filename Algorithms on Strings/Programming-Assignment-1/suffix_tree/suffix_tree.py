# python3
import sys

class Node():
    def __init__(self, start_ind, length, node_id):
        self.start_ind = start_ind
        self.length = length
        self.node_id = node_id
        self.children = []

def merge_nodes(node):
    if node.node_id != 0 and len(node.children) == 1:
        while len(node.children) == 1:
            node.length += node.children[0].length
            node_temp = node.children[0]
            node.children = node.children[0].children[:]
            del node_temp
    
    for sub_node in node.children:
        merge_nodes(sub_node)

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
    str_len = len(text)
    n = 1
    for i in range(str_len):
        for j in range(i, str_len):
            current_node = trie_root
            for k in range(i, j + 1):
                current_symbol = text[k]
                for node in current_node.children:
                    if text[node.start_ind] == current_symbol:
                        current_node = node
                        break
                else:
                    current_node.children.append(Node(k, 1, n))
                    n += 1
    merge_nodes(trie_root)
    cat_to_result(trie_root, text, result)
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
